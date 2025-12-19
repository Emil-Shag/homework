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
        with open(file_path, "r", encoding="UTF-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                logger.info(f"Транзакции успешно загружены из файла: {file_path}")
                return data
            else:
                logger.warning(f"Данные в файле {file_path} не являются списком.")
                return []
    except (FileNotFoundError, json.JSONDecodeError):
        logger.error(f"Ошибка при декодировании JSON из файла {file_path}, либо файл не найден")
        return []
