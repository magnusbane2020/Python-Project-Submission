from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login_to_midway(driver, username, password):
    """Automate the Midway authentication process."""
    driver.get('https://midway-auth.amazon.com')
    try:
        username_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, 'user_name'))
        )
        password_input = driver.find_element(By.ID, 'password')
        login_button = driver.find_element(By.ID, 'verify_btn')
        username_input.send_keys(username)
        password_input.send_keys(password)
        login_button.click()
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, 'page'))
        )
    except Exception as e:
        print(f"Error during login: {e}")
        driver.quit()
        raise
