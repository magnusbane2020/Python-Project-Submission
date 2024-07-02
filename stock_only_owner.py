import requests
import pandas as pd
from threading import Thread
import time
from _dictionaries import dictionary  # Assuming this module contains the dictionaries

def request_stock_encumb(asin: str, marketplaceId: int, merchantid: int) -> None:
    token_manual = ''  # Initialize with an empty string
    with open('./token.txt') as f:
        token_manual = f.readline().strip()  # Read token from file and strip newline

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Authorization': token_manual,
        'Origin': 'https://prod.eu.denali.scot.amazon.dev',
        'Connection': 'keep-alive',
        'Referer': 'https://prod.eu.denali.scot.amazon.dev/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
    }

    params = {
        'fnsku': asin,
    }

    response = requests.get('https://api.prod.eu.denali.scot.amazon.dev/inventory-levels', params=params, headers=headers)

    if response.status_code == 401:
        print(f"Error fetching data for ASIN {asin}, Marketplace ID {marketplaceId}. Status code: 401")
        return

    response_json = response.json()
    print(response_json)

    stock = 0
    encumb = 0

    for item in response_json.get('inventoryLevelByOwnerList', []):
        if item.get('iogId') == dictionary.owner_id.get(marketplaceId):
            stock += item.get('onHand', 0)

    done.append((asin, marketplaceId, stock, encumb))


if __name__ == "__main__":
    df = pd.read_excel('./input folder/input_sheet.xlsx', sheet_name='STOCK')

    if df.empty:
        print("DataFrame 'df' is empty. Please check your input data.")
        exit()

    done = []
    task_list = [(df.loc[i, 'ASIN'], dictionary.marketplace_id.get(df.loc[i, 'MARKETPLACE']), dictionary.merchant_id.get(df.loc[i, 'MARKETPLACE']))
                 for i in range(len(df)) if df.loc[i, 'MARKETPLACE'] in dictionary.available_mps]

    print(task_list)

    threads = []
    for task in task_list:
        thread = Thread(target=request_stock_encumb, args=(task[0], task[1], task[2]))
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    # Print done list for debugging
    print("Done List:")
    for item in done:
        print(item)

    df_exp = pd.DataFrame(columns=['MP', 'ASIN', 'STOCK', 'ENC'])
    inverse_mp_dict = {value: key for key, value in dictionary.marketplace_id.items()}

    for i in range(len(done)):
        mp_name = inverse_mp_dict.get(done[i][1], 'Unknown')
        df_exp.loc[i, 'MP'] = mp_name
        df_exp.loc[i, 'ASIN'] = done[i][0]
        df_exp.loc[i, 'STOCK'] = done[i][2]
        df_exp.loc[i, 'ENC'] = done[i][3]

    df_exp.to_excel("stock_local.xlsx", index=False)
    print('Data saved to stock_local.xlsx successfully.')
