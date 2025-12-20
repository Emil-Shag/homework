import re
from collections import Counter


def process_bank_search(data:list[dict], search:str)->list[dict]:
    """Фильтрация операций по поисковому запросу в описании"""
    pattern = re.compile(search, flags=re.IGNORECASE)
    filtered_transactions = [t for t in data if pattern.search(t.get("description", "").lower())]
    return filtered_transactions

def process_bank_operations(data:list[dict], categories:list)->dict:
    """Подсчёт количества операций по категориям"""
    description_list =[]
    for operation in data:
        if operation.get("description") in categories:
            description_list.append(operation.get("description"))
    count_category = dict(Counter(description_list))
    return count_category
