from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def setup_driver(download_dir):
    """Setup Chrome WebDriver with custom options."""
    chrome_options = Options()
    prefs = {
        "profile.default_content_settings.popups": 0,
        "download.default_directory": download_dir,
        "directory_upgrade": True
    }
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_experimental_option("prefs", prefs)
    # Add the argument to start in full screen
    chrome_options.add_argument("--start-fullscreen")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver
