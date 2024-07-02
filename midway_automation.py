from driver_setup import setup_driver
from authentication import login_to_midway
from cookie_handling import accept_cookies
from navigation import navigate_to_page, custom_function, close_driver, rename_downloaded_file, run_python_script
import pyautogui
class MidwayAutomation:
    def __init__(self, download_dir, username, password):
        self.download_dir = download_dir
        self.username = username
        self.password = password
        self.driver = setup_driver(download_dir)

    def login(self):
        login_to_midway(self.driver, self.username, self.password)

    def accept_cookies(self):
        accept_cookies(self.driver)

    def navigate_to_page(self, url, forecasting_group, email):
        navigate_to_page(self.driver, url, lambda driver: custom_function(driver, forecasting_group, email))
        rename_downloaded_file(self.download_dir, "Forecasting.xlsx")
    def close_driver(self):
        close_driver(self.driver)

    def run_python_script(self, script_path):
        run_python_script(script_path)
