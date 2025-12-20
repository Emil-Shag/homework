import csv

import pandas as pd


def csv_reader(csv_file_path):
    """Функция для считывания финансовых операций из CSV"""
    transactions = []

    with open(csv_file_path, encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=";")

        for row in reader:
            if not row.get("id"):  # пропускаем пустые строки
                continue
            transactions.append(
                {
                    "id": int(row["id"]),
                    "state": row["state"],
                    "date": row["date"],
                    "description": row.get("description", ""),
                    "from": row.get("from"),
                    "to": row.get("to"),
                    "amount": float(row["amount"]),
                    "currency": row["currency_code"],
                }
            )

    return transactions


def exl_reader(exl_file_path):
    """Функция для считывания финансовых операций из Excel"""
    df = pd.read_excel(exl_file_path)
    transactions = []
    for _, row in df.iterrows():
        if pd.isna(row["id"]):
            continue
        transactions.append(
            {
                "id": int(row["id"]),
                "state": row["state"],
                "date": row["date"],
                "description": row.get("description", ""),
                "from": row.get("from"),
                "to": row.get("to"),
                "amount": float(row["amount"]),
                "currency": row["currency_code"],
            }
        )
    return transactions
