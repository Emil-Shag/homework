import csv
import pandas as pd

def csv_reader(csv_file_path):
    with open(csv_file_path, encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=';')
        return list(reader)

def exl_reader(exl_file_path):
    df = pd.read_excel(exl_file_path)
    xls_data = df.to_dict('records')
    return xls_data