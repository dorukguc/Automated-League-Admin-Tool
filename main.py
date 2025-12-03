import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
import os
import re

# 1. SETUP: Define scope and authenticate using JSON key
# Note: The JSON key is not included in this repo for security reasons.
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
json_file_path = "credentials/service_account_key.json" 

try:
    creds = ServiceAccountCredentials.from_json_keyfile_name(json_file_path, scope)
    client = gspread.authorize(creds)
except FileNotFoundError:
    print("Error: JSON key file not found. Please check the credentials path.")
    exit()

# 2. CONFIGURATION: Open the Master Sheet
# Using a placeholder URL for privacy
sheet_url = "https://docs.google.com/spreadsheets/d/YOUR_SHEET_ID_HERE/edit"
spreadsheet = client.open_by_url(sheet_url)

# 3. FILE MANAGEMENT: Create a folder for outputs
target_folder = "csv_output"
if not os.path.exists(target_folder):
    os.makedirs(target_folder)

# 4. DATA PROCESSING: Get the last 45 tabs (Tournaments)
all_worksheets = spreadsheet.worksheets()
# Assuming the relevant tournament tabs are at the end
target_tabs = all_worksheets[-45:] 

print(f"Starting download process for {len(target_tabs)} sheets...")

for sheet in target_tabs:
    try:
        # Read data from Sheet
        data = sheet.get_all_records()
        df = pd.DataFrame(data)

        # Clean the file name using Regex (Remove illegal characters)
        clean_name = re.sub(r'[\\/*?:"<>|]', "_", sheet.title)
        
        # Save as CSV with correct naming convention
        file_name = f"Tournament_{clean_name}.csv"
        full_path = os.path.join(target_folder, file_name)
        
        df.to_csv(full_path, index=False, encoding="utf-8-sig")
        print(f"Successfully saved: {file_name}")
        
    except Exception as e:
        print(f"Error processing sheet {sheet.title}: {e}")

print("All files downloaded and organized.")
