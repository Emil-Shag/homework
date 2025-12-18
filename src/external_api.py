import os

import requests
from dotenv import load_dotenv

load_dotenv()


def transaction_amount_in_rub(transaction):
    """Функция, представляющая транзакции в рублях"""
    amount = transaction["operationAmount"]["amount"]
    currency = transaction["operationAmount"]["currency"]["code"]
    if currency == "RUB":
        return float(amount)

    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"

    headers = {"apikey": os.getenv("API_KEY")}
    payload = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    if response.status_code == 200:
        return float(response.json()["result"])
    else:
        return "Обращение к внешнему API не состоялось"
