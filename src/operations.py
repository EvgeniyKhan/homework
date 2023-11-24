import re
from collections import Counter
from typing import List, Dict


def filter_operations_by_descriptions(operations: List[Dict[str, str]],
                                      search_string: str) -> List[Dict[str, str]]:
    """
    Фильтрует список операций по описанию.
    :param operations: Список словарей с данными о банковских операций
    :param search_string: Строка для поиска операций
    :return: Отфильтрованный список операций
    """
    return [operation for operation in operations
            if re.search(search_string, operation.get("description", ""), re.IGNORECASE)]


def count_operations_by_category(operations: List[Dict[str, str]],
                                 categories: Dict[str, str]) -> Counter:
    """
    Считает количество операций по категориям
    :param operations: Список словарей с данными о банковских операциях
    :param categories: Словарь с категориями операций
    :return: Counter с количеством операций по категориям
    """
    return Counter(operation.get("category", "")
                   for operation in operations if operation.get("category", "") in categories)
