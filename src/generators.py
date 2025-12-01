def filter_by_currency(transactions: list[dict], currency: str) -> dict:
    """Генератор, который фильтрует транзакции по заданной валюте"""
    for transaction in transactions:
        if transaction.get("operationAmount").get("currency").get("code") == currency:
            yield transaction

def transaction_descriptions(transactions: list[dict]) -> str:
    """Генератор, принимает список словарей с транзакциями и возвращает описание каждой операции по очереди."""
    for transaction in transactions:
        yield transaction.get("description")

def card_number_generator(start_value: int, finish_value: int) -> str:
    """Генератор, который выдает номера банковских карт"""
    for i in range(start_value, finish_value + 1):
        zero_amount = 16 - len(str(i))
        card_number = zero_amount * "0" + str(i)
        divided_card_number = card_number[:4] + " " + card_number[4:8] + " " + card_number[8:12] + " " + card_number[12:16]
        yield divided_card_number