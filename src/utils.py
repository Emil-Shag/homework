import json
import logging

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("logs/utils.log", mode="w", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)

file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)

logger.addHandler(file_handler)


def get_transactions_from_file(file_path):
    """Функция, принимающая путь до JSON-файла и возвращает список словарей с данными"""
    try:
        with open(file_path, encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, list):
            logger.warning(f"Данные в файле {file_path} не являются списком.")
            return []

        transactions = []

        for t in data:
            try:
                transactions.append(
                    {
                        "id": t.get("id"),
                        "state": t.get("state"),
                        "date": t.get("date"),
                        "description": t.get("description", ""),
                        "from": t.get("from"),
                        "to": t.get("to"),
                        "amount": float(t["operationAmount"]["amount"]),
                        "currency": t["operationAmount"]["currency"]["code"],
                    }
                )
            except (KeyError, TypeError, ValueError):
                logger.warning(f"Пропущена некорректная транзакция: {t}")

        return transactions

    except (FileNotFoundError, json.JSONDecodeError):
        logger.error(f"Ошибка чтения JSON-файла: {file_path}")
        return []
