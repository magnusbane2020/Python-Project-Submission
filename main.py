import pandas as pd
from midway_automation import MidwayAutomation
import subprocess
import os
from Raport_one import main as run_new_script  # Importăm funcția main din noul script
from datetime import datetime, timezone, timedelta
import pytz


def run_new_script_and_process_results():
    data_file = 'Data.txt'
    report_file = 'Report1.xlsx'
    forecasting_directory = '.'
    forecasting_pattern = 'Forecasting.xlsx_*'
    combined_local_file = 'combined_local.xlsx'
    stock_paneu_file = 'stock_paneu.xlsx'

    # Rulăm noul script pentru a genera raportul și a procesa datele
    run_new_script(data_file, report_file, forecasting_directory, forecasting_pattern, combined_local_file, stock_paneu_file)

    # Aici puteți adăuga cod suplimentar pentru a manipula rezultatele, dacă este cazul
    # De exemplu, puteți trimite raportul prin email sau alte operațiuni.


if __name__ == "__main__":
    data = pd.read_excel('Data.xlsx')
    download_dir = 'C:\\Users\\straduca\\PycharmProjects\\RBS_Python\\TheProject\\'
    username = data['Username'].iloc[0]
    password = data['Password'].iloc[0]
    forecasting_group = data['ForecastingGroup'].iloc[0]
    email = data['Email'].iloc[0]

    midway_automation = MidwayAutomation(download_dir, username, password)
    midway_automation.login()
    midway_automation.accept_cookies()
    test_url = 'https://eu.forecasting-portal.scot.amazon.dev/downloads/create'
    midway_automation.navigate_to_page(test_url, forecasting_group, email)
    midway_automation.close_driver()

    # Path to the Python script you want to execute
    python_script_path = 'C:\\Users\\straduca\\PycharmProjects\\RBS_Python\\TheProject\\stock_denali.py'
    midway_automation.run_python_script(python_script_path)

    # Run the .exe script
    exe_path = 'C:\\Users\\straduca\\PycharmProjects\\RBS_Python\\TheProject\\stock_enc_automation.exe'
    token_path = 'C:\\Users\\straduca\\PycharmProjects\\RBS_Python\\TheProject\\token.txt'

    try:
        result = subprocess.run([exe_path, token_path], check=True, capture_output=True, text=True)
        print(f"Output:\n{result.stdout}")
        print(f"Errors:\n{result.stderr}")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running the .exe script: {e}")

    # Rulăm noul script și procesăm rezultatele sale
    run_new_script_and_process_results()
