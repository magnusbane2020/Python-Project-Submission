# Python-Project-Submission
My project is aimed to create multiple nonstandard reports


Standard Operating Procedure (SOP) for Running Stefan Automation

Table of Contents
1.	Introduction
2.	Prerequisites
3.	Environment Setup
4.	Modules and Functions Description
5.	Step-by-Step Execution
1. Introduction
This SOP outlines the steps to run the Midway Automation script. The script automates various web interactions such as login, cookie acceptance, page navigation, and file handling for the Midway platform.
2. Prerequisites
Before running the script, ensure you have the following:
•	Python 3.x installed on your system.
•	Required Python packages installed.
•	Appropriate WebDriver for your browser installed.
•	Input data in the specified Excel file (Data.xlsx).
•	Correct directory structure.
3. Environment Setup
1.	Install Python Packages: Ensure you have the necessary Python packages installed. You can install them using pip:
 
2.	  Download WebDriver: Download the appropriate WebDriver for your browser (e.g., ChromeDriver for Chrome) and ensure it is accessible from your PATH.

3.	  Directory Structure: Ensure your project directory is structured as follows:
 
4. Modules and Functions Description
4.1. midway_automation.py
Contains the main class MidwayAutomation that orchestrates the automation.
•	Class: MidwayAutomation
o	__init__(self, download_dir, username, password): Initializes the WebDriver and user credentials.
o	login(self): Logs into the Midway portal.
o	accept_cookies(self): Accepts cookies on the Midway portal.
o	navigate_to_page(self, url, forecasting_group, email): Navigates to a specific page and executes custom functions.
o	close_driver(self): Closes the WebDriver.
o	run_python_script(self, script_path): Runs an external Python script.
4.2. authentication.py
Handles user login.
•	Function: login_to_midway(driver, username, password): Automates the login process.
4.3. cookie_handling.py
Handles cookie acceptance.
•	Function: accept_cookies(driver): Handles cookie consent if prompted.
4.4. navigation.py
Handles page navigation and custom interactions.
•	Function: navigate_to_page(driver, url, custom_function=None): Navigates to a given URL and executes a custom function.
•	Function: custom_function(driver, forecasting_group, email): Performs custom actions on the page.
•	Function: rename_downloaded_file(download_dir, new_file_prefix="Forecasting"): Renames the most recently downloaded file.
•	Function: run_python_script(script_path): Runs a Python script.

5. Step-by-Step Execution
Step 1: Initialize and Setup
1.	Prepare Input Data:
o	Ensure Data.xlsx contains the necessary input data (Username, Password, Forecasting Group, Email).
2.	Prepare the token.txt
o	Ensure that the token is new because have a 15 minutes valability.
3.	Prepare the ASIN list 
o	Copy-paste ASIN in Data.txt

Troubleshooting and Tips
1.	Common Issues:
o	Ensure the WebDriver is compatible with the browser version.
o	Verify that element locators (e.g., XPaths) are up-to-date.
2.	Debugging:
o	Print statements are added to log progress and errors.
o	Check console output for any exceptions or errors.


