def filter_by_state(dicts_list: list[dict], state_filter: str="EXECUTED") -> list[dict]:
    """Функция, сортирующая словари по ключу state."""
    sorted_list = []
    for operation in dicts_list:
        if operation["state"] == state_filter:
            sorted_list.append(operation)
    return sorted_list


def sort_by_date(dicts_list: list[dict], descending_sort: bool=True) -> list[dict]:
    """Функция, сортирующая словари по дате"""
    sorted_by_date = sorted(dicts_list, key=lambda operation: operation["date"], reverse=descending_sort)
    return sorted_by_date
