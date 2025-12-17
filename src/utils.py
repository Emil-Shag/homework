import json

def get_transactions_from_file(file_path):
    """Функция, принимающая путь до JSON-файла и возвращает список словарей с данными"""
    with open(file_path, "r", encoding="utf-8") as file:
        try:
            data = json.load(file)
            if not isinstance(data, list):
                return []
            else:
                return data
        except FileNotFoundError:
            return []
