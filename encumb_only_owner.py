import requests
import pandas as pd
import openpyxl
import requests
from threading import Thread
import time
df = pd.read_excel('./input folder/input_sheet.xlsx', sheet_name= 'ENCUMB')
err = [2]
token_manual =  0 
print("starting")
with open('./token.txt') as f:
  line = f.readline()
  token_manual = line 

#print(token_manual)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Authorization': token_manual ,
    'Origin': 'https://prod.eu.denali.scot.amazon.dev',
    'Connection': 'keep-alive',
    'Referer': 'https://prod.eu.denali.scot.amazon.dev/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
}

done = []
response2 = requests.get('https://api.prod.eu.denali.scot.amazon.dev/inventory-levels', headers= headers)
if response2.status_code == 401:
    print("PLEASE UPDATE YOUR TOKENM, CURRENT TOKEN IS EXPIRED")
    time.sleep(2222)

done = []

def request_stock_encumb(asin : str, marketplaceId : int, merchantid : int) -> tuple:
    token = 'Bearer eyJ0eXAiOiJKV1MiLCJhbGciOiJSUzI1NiIsImtpZCI6IjEzNzk4NDM4In0.eyJpc3MiOiJodHRwczovL21pZHdheS1hdXRoLmFtYXpvbi5jb20iLCJzdWIiOiJhbGV4YWlmciIsImF1ZCI6Imh0dHBzOi8vcHJvZC5ldS5kZW5hbGkuc2NvdC5hbWF6b24uZGV2IiwiZXhwIjoxNjk1ODA3NjkyLCJpYXQiOjE2OTU4MDY3OTIsImF1dGhfdGltZSI6MTY5NTgwMDY2Nywibm9uY2UiOiJpemx0NmFodjdsZTZ0NW5vNWIzZnQiLCJhbXIiOiJbXCJwaW5cIiwgXCJ1MmZcIl0iLCJ0cnVzdF9zY29yZSI6bnVsbCwicmVxX2lkIjpudWxsLCJtaWR3YXlfdHJ1c3Rfc2NvcmUiOm51bGwsImFwZXNfcmVzdWx0cyI6bnVsbCwiaWFsIjowLCJhYWwiOjAsImp0aSI6Ikx3ZUpvaFgxN0JCbGk4YlNtZkhoQWc9PSIsInBvc3R1cmVfY2hlY2siOjAsIm13aSI6MH0.MRqKGcS8oOfIX2oej2v9C3gU98qgB9SbXlmhNYLDcLrG-Qp2h_1c_MjdM1izpOovexa9i-o902AM-Ai4IzjU1oTrKqBMrhtNWLF-l9Q_HBzVGaf1zTnfHpakhtKTADp8pIzrFoWe1NEZVIgFqpGTgzfxEGCpIgr15X4eg8hB6O4KhmNlJIRjmL3OBUyt8WHQRUvsV6OTQT-W6c8Y74UZ-n7fsAoxDtJxisSvuQ2HILguAIHkGd86P4ag80PU8Xs4-v9bKsDYky1dskBGd7wUkOSSvxm7pepPIPwQIsihCieajZ904mbDJQRlYtTrf5DUWJ34Sdujie4vAJHI5D8lqQ'
    token = token_manual
    asin = asin
    merchantid = merchantid
    marketplaceId = marketplaceId

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.5',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Authorization': token ,
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

    response = requests.get('https://api.prod.eu.denali.scot.amazon.dev/encumbrance-snapshots-by-type', params=params, headers=headers)
    print(response)
    response = response.json()



    stock : int = 0
    encumb : int = 0



    #print(dictionary.owner_id)
    for item in response['planned']:
        if item['ownerId'] == dictionary.owner_id[marketplaceId]:
            encumb += item['requiredQuantity']

    done.append((asin, marketplaceId, stock, encumb))

    return 0
import time
if __name__ == "__main__":
    
    task_list = []
    from _dictionaries import dictionary
    for i in range(len(df)):

        task_list.append((df['ASIN'][i], dictionary.marketplace_id[df['MARKETPLACE'][i]], dictionary.merchant_id[df['MARKETPLACE'][i]]))



    threads = []
    for task in task_list:
        thread = Thread(target=request_stock_encumb, args=(task[0],task[1],task[2]))
        threads.append(thread)

  
    for thread in threads:
       
        thread.start()
       
    
    for thread in threads:
        
        thread.join()
        

        


df_exp = pd.DataFrame(columns = ['MP','ASIN','STOCK','ENC'])
inverse_mp = dictionary.marketplace_id
inverse_mp_dict = {value: key for (key, value) in inverse_mp.items()} 

for i in range(len(done)):
    df_exp.loc[i,'MP'] = inverse_mp_dict[done[i][1]]
    df_exp.loc[i,'ASIN'] = done[i][0]
    df_exp.loc[i,'STOCK'] = done[i][2]
    df_exp.loc[i,'ENC'] = done[i][3]



df_exp.to_excel("encumb_local.xlsx")
