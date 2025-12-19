from unittest.mock import mock_open, patch

import pandas as pd

from src.new_format_data_reader import csv_reader, exl_reader


@patch(
    "src.new_format_data_reader.open",
    new_callable=mock_open,
    read_data="id;state;date\n650703;EXECUTED;2023-09-05T11:30:32Z\n3598919;EXECUTED;2020-12-06T23:00:58Z\n",
)
def test_csv_reader(mock_file):
    result = csv_reader("test.csv")
    assert result == [
        {"id": "650703", "state": "EXECUTED", "date": "2023-09-05T11:30:32Z"},
        {"id": "3598919", "state": "EXECUTED", "date": "2020-12-06T23:00:58Z"},
    ]
    mock_file.assert_called_once_with("test.csv", encoding="utf-8")


@patch("src.new_format_data_reader.pd.read_excel")
def test_excel_reader(mock_file_xls):
    df = pd.DataFrame(
        [
            {"id": "650703", "state": "EXECUTED", "date": "2023-09-05T11:30:32Z"},
            {"id": "3598919", "state": "EXECUTED", "date": "2020-12-06T23:00:58Z"},
        ]
    )
    mock_file_xls.return_value = df
    result = exl_reader("test.xlsx")
    assert result == [
        {"id": "650703", "state": "EXECUTED", "date": "2023-09-05T11:30:32Z"},
        {"id": "3598919", "state": "EXECUTED", "date": "2020-12-06T23:00:58Z"},
    ]
    mock_file_xls.assert_called_once_with("test.xlsx")
