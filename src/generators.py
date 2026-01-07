from typing import Generator, Iterator


def filter_by_currency(transactions: list[dict], currency: str) -> Iterator:
    """Генератор, который фильтрует транзакции по заданной валюте"""
    if len(transactions) == 0:
        yield "Пустой список"
    for transaction in transactions:
        if transaction.get("currency") == currency:
            yield transaction


def transaction_descriptions(transactions: list[dict]) -> Iterator:
    """Генератор, принимает список словарей с транзакциями и возвращает описание каждой операции по очереди."""
    if len(transactions) == 0:
        yield "Пустой список"
    for transaction in transactions:
        yield transaction.get("description")


def card_number_generator(start_value: int, finish_value: int) -> Generator:
    """Генератор, который выдает номера банковских карт"""
    for i in range(start_value, finish_value + 1):
        zero_amount = 16 - len(str(i))
        card_number = zero_amount * "0" + str(i)
        divided_card_number = (
            card_number[:4] + " " + card_number[4:8] + " " + card_number[8:12] + " " + card_number[12:16]
        )
        yield divided_card_number
