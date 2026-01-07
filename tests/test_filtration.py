from src.filtration import process_bank_search, process_bank_operations


def test_process_bank_search():
    data = [
        {"description": "Перевод организации"},
        {"description": "Перевод на другой счет"},
        {"description": "Открытие счета"},
    ]
    result = process_bank_search(data, "перевод")
    assert result == [
        {"description": "Перевод организации"},
        {"description": "Перевод на другой счет"},
    ]


def test_process_bank_operations():
    data = [
        {"description": "Перевод"},
        {"description": "Перевод"},
        {"description": "Открытие"},
        {"description": "Снятие"},
    ]
    categories = ["Снятие", "Перевод"]

    result = process_bank_operations(data, categories)
    assert result == {
        "Снятие": 1,
        "Перевод": 2,
    }
