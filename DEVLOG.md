# Development Log and Technical Notes

This document tracks my active development process, the technical challenges I faced, and the solutions I implemented.

Since I am actively learning Python, I used AI tools throughout this project. I designed with AI the automation logic and workflow. Using AI to assist with syntax generation, debugging errors, and finding optimal libraries.

---

### [03.12.2025] - Phase 2: Selenium Integration (Work in Progress)
**Status:** Login and Menu Navigation implemented.

**The Workflow & Challenges:**

**1. Designing the Login Logic:**
* **Goal:** I needed the bot to open Chrome and log in automatically.
* **My Role:** I identified that I needed the `Selenium` library for browser automation.
* **AI Assistance:** I asked AI how to target input fields reliably. It suggested using `By.ID` for static elements.
* **Result:** I successfully implemented the login function.

**2. Handling the "Sign In" Button:**
* **Challenge:** The login button did not have an ID, so the standard code failed.
* **Solution Process:** I consulted AI for alternative ways to find elements. It explained `By.XPATH` and how to find buttons by their text. I applied this logic to the script, and it worked.

**3. Handling Dynamic Menus:**
* **Challenge:** The bot was trying to click menus before they loaded, causing crashes.
* **Solution Process:** I researched "how to make Selenium wait" and used AI to understand the difference between `time.sleep` (static wait) and `WebDriverWait` (dynamic wait). I chose `WebDriverWait` for better performance.

---

### [22.05.2025] - Phase 1: Batch Downloader
**Status:** Completed.

**The Workflow & Challenges:**

**1. Connecting to Google Sheets:**
* **Goal:** Download data from 45 different tabs automatically.
* **My Role:** I decided to use the Google Sheets API instead of downloading files manually.
* **AI Assistance:** I used AI to generate the boilerplate code for `gspread` authentication, as the API documentation was complex for a beginner.

**2. File Naming Logic:**
* **Challenge:** Some sheet names contained symbols like `/` or `:`, which caused file creation errors in Windows.
* **Solution Process:** I realized I needed to clean the text. I asked AI for a Regex pattern to remove illegal characters. I integrated this pattern into my loop to ensure every file is saved correctly.
