# Web Scraper for Class Update Patch Notes

## Description

This Python script scrapes patch notes from the Black Desert Online website and stores the extracted text in a MongoDB database. It is designed to fetch a range of patch notes based on configurable release numbers, filter the text for relevant class updates, and display meaningful information in the terminal.

## Features

- **Web Scraping:** Extracts text content from patch note pages.
- **MongoDB Storage:** Stores scraped content to prevent duplicate entries.
- **Configurable Settings:** Allows users to adjust release numbers and display preferences.
- **Filtering and Formatting:** Extracts and formats relevant content like class changes.
- **Automated MongoDB Check:** Verifies if MongoDB is running before execution.

## Installation

### Prerequisites

Ensure you have the following installed:

- Python 3.x
- MongoDB
- Required Python packages:
  ```sh
  pip install requests beautifulsoup4 pymongo
  ```

## Usage

### Configuration

Modify the following variables at the beginning of the script:

```python
RELEASE_NUMBER = 8096  # Latest release number
PAST_RELEASE = 8000  # Oldest release number to scrape
DISPLAY_UPDATE_TEXT = False  # Set to True to display extracted content
DISPLAY_LARGE_UPDATES = False  # Set to True to display large updates
```
You can find the most recent **Release_Number** by going to 
https://www.naeu.playblackdesert.com/en-US/News/Notice?boardType=2  
and then hovering the desired Patch Notes.  
This will determine the starting point for our webscraper.
![image](https://github.com/user-attachments/assets/dddf278c-aabf-4011-8f1c-de4f0838339f)  
**Past_Release** is the amount of Websites we want to check,  
Pearl Abyss is hosting Patch Notes dating all the way back to 2021.

### Running the Script

Start MongoDB before running the script. Then execute:

```sh
python script.py
```

## Output

- The script will fetch and store patch note data in MongoDB.
- It will list the URLs where class changes occurred.
- If `DISPLAY_UPDATE_TEXT` is enabled, it will print extracted class changes.

![image](https://github.com/user-attachments/assets/fccb6ed3-0d20-4290-9acd-97624094345f)


## Future Enhancements

- Filter updates by class name.
- Build a frontend UI for easier navigation.
- Host as a web-based service.

## Troubleshooting

- Ensure MongoDB is running:
  ```sh
  mongod
  ```
- Check MongoDB connection settings if the script fails to connect.
- If no updates appear, adjust `RELEASE_NUMBER` and `PAST_RELEASE` values.

## License

This project is open-source and available for modification.

## Author

Developed by Ottitsch. Contributions are welcome!
