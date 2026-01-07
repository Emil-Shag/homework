import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(test_transactions_1):
    filtred_operation = filter_by_currency(test_transactions_1, "USD")
    assert next(filtred_operation) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "currency": "USD",
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    assert next(filtred_operation) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "currency": "USD",
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }
    assert next(filtred_operation) == {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "currency": "USD",
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    }


def test_filter_by_currency_3(test_transactions_2):
    filtred_operation = filter_by_currency(test_transactions_2, "USD")
    assert next(filtred_operation) == "Пустой список"


def test_transaction_descriptions_1(test_transactions_1):
    descriptions = transaction_descriptions(test_transactions_1)
    assert next(descriptions) == "Перевод организации"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод с карты на карту"
    assert next(descriptions) == "Перевод организации"


def test_transaction_descriptions_2(test_transactions_2):
    descriptions = transaction_descriptions(test_transactions_2)
    assert next(descriptions) == "Пустой список"


@pytest.mark.parametrize(
    "start_value, finish_value, divided_card_number",
    [
        (
            1,
            5,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
                "0000 0000 0000 0004",
                "0000 0000 0000 0005",
            ],
        ),
        (9999999999999997, 9999999999999999, ["9999 9999 9999 9997", "9999 9999 9999 9998", "9999 9999 9999 9999"]),
    ],
)
def test_card_number_generator_1(start_value, finish_value, divided_card_number):
    result = list(card_number_generator(start_value, finish_value))
    assert result == divided_card_number
