from unittest.mock import mock_open, patch

import pandas as pd

from src.new_format_data_reader import csv_reader, exl_reader


@patch(
    "builtins.open",
    new_callable=mock_open,
    read_data=(
        "id;state;date;amount;currency_code;description;from;to\n"
        "650703;EXECUTED;2023-09-05T11:30:32Z;1000;RUB;Перевод;Счет 1;Счет 2\n"
        "3598919;EXECUTED;2020-12-06T23:00:58Z;500;USD;Оплата;Счет 3;Счет 4\n"
    ),
)
def test_csv_reader(mock_file):
    result = csv_reader("test.csv")

    assert result == [
        {
            "id": 650703,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "description": "Перевод",
            "from": "Счет 1",
            "to": "Счет 2",
            "amount": 1000.0,
            "currency": "RUB",
        },
        {
            "id": 3598919,
            "state": "EXECUTED",
            "date": "2020-12-06T23:00:58Z",
            "description": "Оплата",
            "from": "Счет 3",
            "to": "Счет 4",
            "amount": 500.0,
            "currency": "USD",
        },
    ]

    mock_file.assert_called_once_with("test.csv", encoding="utf-8")


@patch("src.new_format_data_reader.pd.read_excel")
def test_excel_reader(mock_file_xls):
    df = pd.DataFrame(
        [
            {
                "id": "650703",
                "state": "EXECUTED",
                "date": "2023-09-05T11:30:32Z",
                "description": "Перевод",
                "from": "Счет 1",
                "to": "Счет 2",
                "amount": 1000.0,
                "currency_code": "RUB",
            },
            {
                "id": "3598919",
                "state": "EXECUTED",
                "date": "2020-12-06T23:00:58Z",
                "description": "Оплата",
                "from": "Счет 3",
                "to": "Счет 4",
                "amount": 500.0,
                "currency_code": "USD",
            },
        ]
    )
    mock_file_xls.return_value = df
    result = exl_reader("test.xlsx")
    assert result == [
        {
            "id": 650703,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "description": "Перевод",
            "from": "Счет 1",
            "to": "Счет 2",
            "amount": 1000.0,
            "currency": "RUB",
        },
        {
            "id": 3598919,
            "state": "EXECUTED",
            "date": "2020-12-06T23:00:58Z",
            "description": "Оплата",
            "from": "Счет 3",
            "to": "Счет 4",
            "amount": 500.0,
            "currency": "USD",
        },
    ]
    mock_file_xls.assert_called_once_with("test.xlsx")
