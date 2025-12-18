import json


def get_transactions_from_file(file_path):
    """Функция, принимающая путь до JSON-файла и возвращает список словарей с данными"""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            else:
                return []
    except (FileNotFoundError, json.JSONDecodeError):
        return []
