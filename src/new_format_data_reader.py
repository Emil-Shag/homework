import csv

import pandas as pd


def csv_reader(csv_file_path):
    """Функция для считывания финансовых операций из CSV"""
    with open(csv_file_path, encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=";")
        return list(reader)


def exl_reader(exl_file_path):
    """Функция для считывания финансовых операций из Excel"""
    df = pd.read_excel(exl_file_path)
    xls_data = df.to_dict(orient="records")
    return xls_data


a = csv_reader("data/transactions.csv")
print(a)