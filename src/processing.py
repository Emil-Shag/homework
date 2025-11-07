from typing import Union

from src.widget import get_date


def filter_by_state(dicts_list: list[dict], state_filter: str = "EXECUTED") -> list[dict]:
    """Функция, сортирующая словари по ключу state."""
    sorted_list = []
    for operation in dicts_list:
        if operation.get("state") == state_filter:
            sorted_list.append(operation)
        else:
            continue
    return sorted_list


def sort_by_date(dicts_list: list[dict], descending_sort: bool = True) -> Union[list[dict], str]:
    """Функция, сортирующая словари по дате"""
    sorted_by_date = sorted(dicts_list, key=lambda item: item["date"], reverse=descending_sort)
    for items in dicts_list:
        if get_date(items["date"]) == "Неверно указаны параметры даты":
            return "В приведённом списке находятся операции с некорректной датой"
    return sorted_by_date
