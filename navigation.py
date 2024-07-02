import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
import pyautogui
from datetime import datetime , timezone, timedelta
import pytz
import subprocess
def navigate_to_page(driver, url, custom_function=None):
    """Navigate to a given URL and execute a custom function if provided."""
    print(f"Navigating to: {url}")
    driver.get(url)
    wait_time = 1
    start_time = time.time()
    while (time.time() - start_time) < wait_time:
        if custom_function:
            custom_function(driver)
            break
        time.sleep(1)

def click_element(driver, xpath):
    """Click an element identified by xpath."""
    element = driver.find_element(By.XPATH, xpath)
    element.click()

def custom_function(driver, forecasting_group, email):
    """Perform custom actions after navigating to a page."""
    # Your custom actions here, e.g., interacting with web elements
    # This function should include all interactions that need to be performed on the webpage
    print("Executing custom function")
    time.sleep(2)  # Example wait time

    # Click on the first xpath after waiting
    xpath_1 = "/html/body/div/div/div/div/div/a[2]"
    driver.find_element(By.XPATH, xpath_1).click()
    time.sleep(2)

    # Click on the second xpath after waiting
    xpath_2 = "/html/body/div/div/div/div/div[2]/div/div/div/div/button/div/div"
    driver.find_element(By.XPATH, xpath_2).click()
    time.sleep(2)

    # Click on the third xpath after waiting
    xpath_3 = "/html/body/div/div/div/div/div[3]/div/button"
    driver.find_element(By.XPATH, xpath_3).click()
    time.sleep(2)

    # Find the input field by aria-label attribute and send the value from Excel to it
    input_field = driver.find_element(By.XPATH, "//input[@aria-label='Forecasting Group']")
    input_field.clear()  # Clear any existing value in the input field
    input_field.send_keys(str(forecasting_group))

    # Press the Enter key to submit the value
    input_field.send_keys(Keys.ENTER)

    # Click on another element to move the focus away from the input field
    body_element = driver.find_element(By.TAG_NAME, "body")
    ActionChains(driver).move_to_element(body_element).click().perform()

    # Wait for a few seconds
    time.sleep(2)

    # Find the element by XPath and wait for it to be clickable
    xpath_4 = "/html/body/div/div[2]/div/div/div/div/main/div/div[2]/div/form/div/div/div/div[2]/div[2]/div/div/div/div/div[2]/button/span"
    button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath_4)))
    button.click()
    time.sleep(2)

    # Activate the dropdown
    xpath_5 = "/html/body/div/div[2]/div/div/div/div/main/div/div[2]/div/form/div/div/div/div[2]/div[1]/div/div[1]/div/div/div[2]/div/div[3]/div/div/div/div/div/div/div[1]/button"
    button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath_5)))
    button.click()
    time.sleep(2)

    # Simulate pressing the arrow down key once
    ActionChains(driver).send_keys(Keys.ARROW_DOWN).perform()

    # Simulate pressing the Enter key
    ActionChains(driver).send_keys(Keys.ENTER).perform()

    time.sleep(2)

    checkbox_xpath = "/html/body/div/div[2]/div/div/div/div/main/div/div[2]/div/form/div/div/div/div[2]/div[1]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/span[1]/span/span[2]"
    checkbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, checkbox_xpath)))
    # Click on the checkbox
    checkbox.click()
    time.sleep(1)

    checkbox_xpath1 = "/html/body/div/div[2]/div/div/div/div/main/div/div[2]/div/form/div/div/div/div[2]/div[1]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/span[2]/span/span[2]"
    checkbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, checkbox_xpath1)))
    # Click on the checkbox
    checkbox.click()
    time.sleep(1)

    checkbox_xpath2 = "/html/body/div/div[2]/div/div/div/div/main/div/div[2]/div/form/div/div/div/div[2]/div[1]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/span[3]/span/span[2]"
    checkbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, checkbox_xpath2)))
    # Click on the checkbox
    checkbox.click()
    time.sleep(1)

    checkbox_xpath3 = "/html/body/div/div[2]/div/div/div/div/main/div/div[2]/div/form/div/div/div/div[2]/div[1]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/span[4]/span/span[2]"
    checkbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, checkbox_xpath3)))
    # Click on the checkbox
    checkbox.click()
    time.sleep(1)

    checkbox_xpath4 = "/html/body/div/div[2]/div/div/div/div/main/div/div[2]/div/form/div/div/div/div[2]/div[1]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/span[5]/span/span[2]"
    checkbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, checkbox_xpath4)))
    # Click on the checkbox
    checkbox.click()
    time.sleep(1)

    # În loc să folosim clear(), folosim send_keys pentru a selecta și șterge valoarea din câmpul de intrare
    input_field_quantile = driver.find_element(By.XPATH,
                                               "/html/body/div/div[2]/div/div/div/div/main/div/div[2]/div/form/div/div/div/div[2]/div[1]/div/div[3]/div/div/div[2]/div/div[3]/div/div[2]/div/div/div/div/div/input")
    quantile = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                           "/html/body/div/div[2]/div/div/div/div/main/div/div[2]/div/form/div/div/div/div[2]/div[1]/div/div[3]/div/div/div[2]/div/div[3]/div/div[2]/div/div/div/div/div/input")))

    try:
        input_field_quantile.send_keys(Keys.CONTROL + "a")  # Selectează întreaga valoare
        input_field_quantile.send_keys(Keys.DELETE)  # Șterge valoarea selectată
        input_field_quantile.send_keys(str("70"))  # Trimite valoarea "70" în câmpul de intrare
    except ElementNotInteractableException:
        print("Elementul nu poate fi interacționat. Verifică vizibilitatea și interactivitatea acestuia.")
        # Poți adăuga aici și alte acțiuni sau tratamente, cum ar fi așteptări suplimentare sau identificarea unui selector mai specific
    # Click on add button
    xpath_add = "/html/body/div/div[2]/div/div/div/div/main/div/div[2]/div/form/div/div/div/div[2]/div[1]/div/div[3]/div/div/div[2]/div/div[4]/button"
    button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath_add)))
    button.click()
    time.sleep(2)

    # Click on next button
    xpath_6 = "/html/body/div/div[2]/div/div/div/div/main/div/div[2]/div/form/div/div/div/div[2]/div[2]/div/div/div/div/div[3]"
    button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath_6)))
    button.click()
    time.sleep(2)

    # Coosing the list of asins
    upload_file_button = "/html/body/div/div[2]/div/div/div/div/main/div/div[2]/div/form/div/div/div/div[2]/div[1]/div/div/div[2]/div/div[1]/ul/li[2]"
    button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, upload_file_button)))
    button.click()
    time.sleep(2)

    # Click on the choose file button
    choose_file_button = "/html/body/div/div[2]/div/div/div/div/main/div/div[2]/div/form/div/div/div/div[2]/div[1]/div/div/div[2]/div/div[2]/div[2]/div/div[3]/div/div/div/div/div/div[2]/button/span[1]"
    button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, choose_file_button)))
    button.click()
    time.sleep(2)

    # Wait for the file explorer window to open
    time.sleep(2)

    # Type the path of the file you want to upload
    file_path = "C:\\Users\\straduca\\PycharmProjects\\RBS_Python\\TheProject\\Data.txt"  # Replace with the path of your file
    pyautogui.write(file_path)

    # Press Enter to confirm the selection
    pyautogui.press('enter')

    # Wait for the file to be uploaded (adjust the time as needed)
    time.sleep(2)

    # Click on next button
    xpath_7 = "/html/body/div/div[2]/div/div/div/div/main/div/div[2]/div/form/div/div/div/div[2]/div[2]/div/div/div/div/div[3]"
    button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath_7)))
    button.click()
    time.sleep(2)

    # Click on xcel option
    xpath_8 = "/html/body/div/div[2]/div/div/div/div/main/div/div[2]/div/form/div/div/div/div[2]/div[1]/div/div/div[2]/div/div/div/div[2]/div/div/div/div/div/div[1]/button[1]/span"
    button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath_8)))
    button.click()
    time.sleep(2)
    # Click next button
    xpath_9 = "/html/body/div/div[2]/div/div/div/div/main/div/div[2]/div/form/div/div/div/div[2]/div[2]/div/div/div/div/div[3]"
    button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath_9)))
    button.click()
    time.sleep(2)
    # Locate the input field for email and input the value
    input_field_xpath1 = "/html/body/div/div[2]/div/div/div/div/main/div/div[2]/div/form/div/div/div/div[2]/div[1]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/div/input"

    # Locate the element again to avoid stale element reference
    input_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, input_field_xpath1)))

    try:
        input_field.clear()
    except Exception as e:
        print(f"Error clearing input field: {e}")

    # Send the email to the input field
    input_field.send_keys(email)
    time.sleep(2)

    # Move the focus away from the email input field to avoid any auto-submission or page reloads
    body_element.click()
    time.sleep(2)

    # Proceed to click the next button
    next_button_xpath = "/html/body/div/div[2]/div/div/div/div/main/div/div[2]/div/form/div/div/div/div[2]/div[2]/div/div/div/div/div[3]"
    next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, next_button_xpath)))
    next_button.click()
    time.sleep(2)
    # steps for downloading the file
    reset_button_xpath = "/html/body/div/div[2]/div/div/div/div/main/div/div[2]/div/div/div/div[1]/div/div/div[1]/div/div[2]/div/div[1]"
    table_xpath = "/html/body/div/div[2]/div/div/div/div/main/div/div[2]/div/div/div/div[2]/div[1]/table/tbody"

    # Funcția pentru așteptarea linkului și pentru a face clic pe el
    def wait_for_link_and_click(driver):
        # Get current time with timezone
        script_start_time = datetime.now(timezone.utc)
        print(f"Script started at: {script_start_time}")

        seen_links = set()

        while True:
            # Click pe butonul de reset
            reset_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, reset_button_xpath)))
            reset_button.click()
            time.sleep(2)

            # Verificarea statusului linkului
            table_element = driver.find_element(By.XPATH, table_xpath)
            rows = table_element.find_elements(By.TAG_NAME, "tr")

            if not rows:
                print("No rows found, retrying...")
                time.sleep(2)
                continue

            for row in rows:
                cells = row.find_elements(By.TAG_NAME, "td")

                # Verificăm dacă lista cells are cel puțin două elemente
                if len(cells) < 2:
                    continue

                creation_date = cells[1].text
                status_text = cells[3].text

                # Parse creation date with timezone
                creation_date_dt = datetime.strptime(creation_date,
                                                     '%a %b %d %Y %H:%M:%S GMT%z (Eastern European Summer Time)')

                # Verificare dacă creation date este cu cel puțin 2 minute după script_start_time
                if creation_date_dt > script_start_time + timedelta(minutes=2):
                    link_element = None
                    try:
                        link_element = cells[0].find_element(By.TAG_NAME, "a")
                    except NoSuchElementException:
                        pass

                    if link_element:
                        link_text = link_element.text
                        if link_text in seen_links:
                            print(f"Already seen link: {link_text}, skipping...")
                            continue
                        seen_links.add(link_text)

                        if status_text == "IN-PROGRESS":
                            print("Link status is IN-PROGRESS")
                            break
                        elif status_text == "COMPLETED":
                            print("Link status is COMPLETED")

                            # Scroll to make the element visible
                            driver.execute_script("arguments[0].scrollIntoView(true);", link_element)
                            time.sleep(1)

                            # Click the link using JavaScript
                            driver.execute_script("arguments[0].click();", link_element)
                            time.sleep(10)  # Wait for download to complete (increased to 10 seconds)
                            print("Download finished")
                            return  # Exit the function after downloading

            print(f"No suitable link found, retrying...")

            time.sleep(10)  # Wait before checking again

    # Apelarea funcției pentru așteptarea linkului și pentru a face clic pe el
    wait_for_link_and_click(driver)
    pass

def close_driver(driver):
    """Close the WebDriver."""
    driver.quit()


def rename_downloaded_file(download_dir, new_file_prefix="Forecasting"):
    """Rename the most recently downloaded file with current date and time."""
    time.sleep(5)  # Wait for the download to complete
    files = os.listdir(download_dir)
    files.sort(key=lambda x: os.path.getmtime(os.path.join(download_dir, x)), reverse=True)

    if files:
        most_recent_file = os.path.join(download_dir, files[0])
        current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")  # Format: YYYY-MM-DD_HH-MM-SS
        new_file_name = f"{new_file_prefix}_{current_datetime}.xlsx"
        new_file_path = os.path.join(download_dir, new_file_name)

        try:
            os.rename(most_recent_file, new_file_path)
            print(f"Renamed the file to: {new_file_path}")
        except Exception as e:
            print(f"Error renaming file: {e}")

def run_python_script(script_path):
    """Run a Python script."""
    try:
        result = subprocess.run(['python', script_path], check=True)
        print(f"Executed {script_path} with result: {result}")
    except Exception as e:
        print(f"Error executing {script_path}: {e}")
        raise