import re
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

# USAGE REPLACE RELEASE NUMBER WITH MOST RECENT PATCH NOTES:
RELEASE_NUMBER = 8096
PAST_RELEASE = 8000
# USAGE IF YOU DO NOT WANT TO READ THE ACTUAL CONTENT IN THE TERMINAL SET TO FALSE
DISPLAY_UPDATE_TEXT = False
# USAGE Recommended to keep this off, so that the content remains in a readable size
DISPLAY_LARGE_UPDATES = False


# MongoDB setup
MONGO_URI = "mongodb://localhost:27017"
DATABASE_NAME = "web_scraper_db"
COLLECTION_NAME = "scraped_text"

client = MongoClient(MONGO_URI)
db = client[DATABASE_NAME]
collection = db[COLLECTION_NAME]

# Web scraping function
def scrape_text(url):
    # Check if the URL already exists in the collection
    if collection.find_one({"url": url}):
        print(f"Skipping {url}, already exists in the database.")
        return

    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        # Extract all text from the webpage
        page_text = soup.get_text(separator=" ", strip=True)
        data = {
            "url": url,
            "text": page_text
        }
        collection.insert_one(data)
        print(f"Scraped text stored successfully from {url}")
    else:
        print(f"Failed to fetch the page. Status code: {response.status_code}")

def required_words(text):
    required_words = ["Patch Notes", "Class Changes", "Contents"]
    return all(word in text for word in required_words)

def display_date(text):
    return text.split('|')[0] if '|' in text else text

def cleaned_text(text):
    match = re.search(r'Class Changes(.*?)Contents', text, flags=re.DOTALL)
    return match.group(1) if match else ""

def format_text(text):
    word_count = len(text.split())
    if not DISPLAY_LARGE_UPDATES:
        if word_count > 500:
            return "Not Displaying Large Update to improve Overhead"
    return text.replace('. ', '.\n')


def is_mongodb_running():
    print("Checking if MongoDB is running\nplease wait...")
    try:
        client.admin.command('ping')
        print("MongoDB is running.")
        return True
    except Exception as e:
        print("MongoDB is not running:", e)
        return False

# Checks if mongoDB is Running
if not is_mongodb_running():
    print("Please make sure you install MongoDB")
    exit()

# Iterate over websites and store date in mongoDB
for i in range(RELEASE_NUMBER, PAST_RELEASE, -1):
    url_to_scrape = "https://www.naeu.playblackdesert.com/en-US/News/Detail?groupContentNo=" + str(i) + "&countryType=en-US"
    scrape_text(url_to_scrape)

for i in range(0,5):
    print(" ")

print("Here is a List of Patch Notes where Class Changes happened")
print("If this List is empty Please Adjust RELEASE_NUMBER and PAST_RELEASE\n")

# Fetch and display stored data
for record in collection.find():
    if required_words(record["text"]):
        print(display_date(record["text"]))
        print(record["url"])
        if DISPLAY_UPDATE_TEXT:
            print(format_text(cleaned_text(record["text"])))
        print("-" * 80)



#TODO: ADD FEATURE WHERE IT ONLY DISPLAYS THE CLASS UPDATES FOR A CERTAIN CLASS
#TODO: ADD FRONTEND DISPLAY
#TODO: HOST AS A WEBSITE