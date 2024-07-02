from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def accept_cookies(driver):
    """Handle cookie consent if prompted."""
    try:
        consent_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Accept')]"))
        )
        consent_button.click()
        print("Clicked consent button")
    except Exception as e:
        print(f"No consent button found or other error: {e}")
