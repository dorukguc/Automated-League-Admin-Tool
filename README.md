# Automated League Admin Tool

### The Problem
In my Data Operations role, I manage match schedules for 5 different tournament groups. Each group consists of multiple tournaments, resulting in 45 separate schedule tables located in a master Google Sheets file.

The manual process was extremely time-consuming because Google Sheets does not offer a feature to download all tabs as individual CSV files at once. Every day, I had to:
1. Manually open each of the 45 tabs.
2. Download the active sheet as a CSV file.
3. Rename the file manually based on the specific tournament date and type to avoid confusion.
4. Upload these files one by one to the tournament management website.

This manual routine took approximately 1 hour every day and was prone to human errors, such as incorrect file naming or downloading the wrong tab.

### The Solution (Current Status)
I developed a Python script with AI to completely automate the first half of this workflow (The Download Phase).

The script uses the Google Sheets API to connect to the online spreadsheet. It iterates through all relevant tabs, reads the data using *Pandas*, and automatically saves them as CSV files to a specific folder on my computer.

Crucially, the script uses the data inside the sheet to generate the correct filename automatically. This eliminates naming errors and completes the download process in seconds. This automation currently saves me about 30 minutes of manual work daily.

### Future Improvements (Work in Progress)
I am actively working on automating the second phase: The Upload Process.

My goal is to use Selenium to log in to the tournament management website and upload the 45 downloaded files to their respective locations automatically. This will save the remaining 30 minutes of the manual workload.

Since the website has a complex HTML structure with many nested menus for different groups, I am currently learning HTML and web scraping techniques to build a reliable navigation logic for the bot.

### Technical Details & Tools
* Python 3: The core programming language.
* Pandas: Used to read the spreadsheet data and save it in CSV format without data loss.
* gspread & oauth2client: Used to securely authenticate and connect to the Google Sheets API using a JSON key.
* OS & Re (Regex): Used to create local directories and sanitize file names by removing illegal characters.

### Setup & Usage
To run this project locally:
1. Install Dependencies: pip install -r requirements.txt
2. Google API Setup: Place your Google Service Account JSON key in the credentials folder and update the path in main.py.

*Note: I am currently learning Python and Data Analysis. During this project, I used AI tools to understand how to set up the Google API authentication and to debug file path errors. This project helped me understand how to integrate cloud data with local file systems.*
