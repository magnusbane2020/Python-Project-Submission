import pandas as pd
import os
import glob


def create_report1_from_data(data_file, output_file):
    # Citește datele din Data.txt
    data = pd.read_csv(data_file, header=None, names=['ASIN'])

    # Elimină duplicatelor din DataFrame
    data.drop_duplicates(inplace=True)

    # Creează un DataFrame cu coloanele necesare
    df = pd.DataFrame(data)
    df['GlProductGroup'] = ''
    df['Description'] = ''
    df['ReplenishmentCategory'] = ''
    df['Forecast 4W'] = ''
    df['In Building'] = ''
    df['ENC (In Building)'] = ''
    df['Ussable supplay'] = ''
    df['ENC (Ussable supplay)'] = ''

    # Capurile de tabel
    columns = ['ASIN', 'GlProductGroup', 'Description', 'ReplenishmentCategory',
               'Forecast 4W', 'In Building', 'ENC (In Building)', 'Ussable supplay',
               'ENC (Ussable supplay)']

    # Scrie DataFrame-ul într-un fișier Excel cu capurile de tabel
    df.to_excel(output_file, index=False, columns=columns)


def find_latest_forecasting_file(directory, pattern):
    files = glob.glob(os.path.join(directory, pattern))
    if not files:
        return None
    latest_file = max(files, key=os.path.getctime)
    return latest_file


def vlookup_and_update(report_file, forecasting_file, combined_local_file, stock_paneu_file):
    # Citește fișierele Excel
    report_df = pd.read_excel(report_file)
    forecasting_df = pd.read_excel(forecasting_file, sheet_name='itemDetail')

    # Tipărește coloanele din forecasting_df pentru debugging
    print(f"Columns in itemDetail sheet: {forecasting_df.columns}")

    # Realizează VLOOKUP-ul și adaugă datele în report_df
    merged_df = report_df.merge(forecasting_df[['ASIN', 'GlProductGroup', 'Description', 'ReplenishmentCategory']],
                                on='ASIN', how='left', suffixes=('', '_forecasting'))

    # Înlocuiește coloanele originale cu cele aduse prin VLOOKUP
    merged_df['GlProductGroup'] = merged_df['GlProductGroup'].fillna(merged_df['GlProductGroup_forecasting'])
    merged_df['Description'] = merged_df['Description'].fillna(merged_df['Description_forecasting'])
    merged_df['ReplenishmentCategory'] = merged_df['ReplenishmentCategory'].fillna(
        merged_df['ReplenishmentCategory_forecasting'])

    # Șterge coloanele redundante
    merged_df.drop(
        columns=['GlProductGroup_forecasting', 'Description_forecasting', 'ReplenishmentCategory_forecasting'],
        inplace=True)

    # Citește sheet-ul FinalP70 din forecasting_df
    finalp70_df = pd.read_excel(forecasting_file, sheet_name='FinalP70')

    # Calculăm suma coloanelor C, D, E și F
    finalp70_df['Total'] = finalp70_df.iloc[:, 2:6].sum(axis=1)

    # Realizează VLOOKUP-ul pentru a adăuga Total în Forecast 4W
    merged_df = merged_df.merge(finalp70_df[['ASIN', 'Total']], on='ASIN', how='left', suffixes=('', '_finalp70'))
    merged_df['Forecast 4W'] = merged_df['Forecast 4W'].fillna(merged_df['Total'])
    merged_df.drop(columns=['Total'], inplace=True)

    # Citește fișierul combined_local.xlsx
    combined_local_df = pd.read_excel(combined_local_file)

    # Realizează VLOOKUP-ul pentru coloanele C și D din combined_local.xlsx
    merged_df = merged_df.merge(combined_local_df[['ASIN', combined_local_df.columns[2], combined_local_df.columns[3]]],
                                on='ASIN', how='left', suffixes=('', '_combined'))
    merged_df['In Building'] = merged_df['In Building'].fillna(merged_df[combined_local_df.columns[2]])
    merged_df['ENC (In Building)'] = merged_df['ENC (In Building)'].fillna(merged_df[combined_local_df.columns[3]])
    merged_df.drop(columns=[combined_local_df.columns[2], combined_local_df.columns[3]], inplace=True)

    # Citește fișierul stock_paneu.xlsx
    stock_paneu_df = pd.read_excel(stock_paneu_file)

    # Realizează VLOOKUP-ul pentru coloanele D și E din stock_paneu.xlsx
    merged_df = merged_df.merge(stock_paneu_df[['ASIN', stock_paneu_df.columns[3], stock_paneu_df.columns[4]]],
                                on='ASIN', how='left', suffixes=('', '_stock_paneu'))
    merged_df['Ussable supplay'] = merged_df['Ussable supplay'].fillna(merged_df[stock_paneu_df.columns[3]])
    merged_df['ENC (Ussable supplay)'] = merged_df['ENC (Ussable supplay)'].fillna(merged_df[stock_paneu_df.columns[4]])
    merged_df.drop(columns=[stock_paneu_df.columns[3], stock_paneu_df.columns[4]], inplace=True)

    # Elimină duplicatele
    merged_df.drop_duplicates(inplace=True)

    # Salvăm fișierul actualizat
    merged_df.to_excel(report_file, index=False)


def main(data_file, report_file, forecasting_directory, forecasting_pattern, combined_local_file, stock_paneu_file):
    create_report1_from_data(data_file, report_file)

    latest_forecasting_file = find_latest_forecasting_file(forecasting_directory, forecasting_pattern)

    if latest_forecasting_file:
        print(f"Using latest forecasting file: {latest_forecasting_file}")
        vlookup_and_update(report_file, latest_forecasting_file, combined_local_file, stock_paneu_file)
        print(
            f"Updated {report_file} with data from {latest_forecasting_file}, {combined_local_file}, and {stock_paneu_file}.")
    else:
        print("Nu am găsit niciun fișier forecasting.")


if __name__ == "__main__":
    # Parametrii pentru funcția main pot fi setați aici
    data_file = 'Data.txt'
    report_file = 'Report1.xlsx'
    forecasting_directory = '.'
    forecasting_pattern = 'Forecasting.xlsx_*'
    combined_local_file = 'combined_local.xlsx'
    stock_paneu_file = 'stock_paneu.xlsx'

    main(data_file, report_file, forecasting_directory, forecasting_pattern, combined_local_file, stock_paneu_file)
