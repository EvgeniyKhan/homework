from typing import List, Optional, Dict


def filter_by_state(data: List[Dict[str, str]], state: Optional[str] = "EXECUTED") -> List[Dict[str, str]]:
    """
    Функция, которая принимает на вход список словарей и значение для ключа state (опциональный параметр со значением
     по умолчанию
    EXECUTED)
    :return: Возвращает новый список, содержащий словари с ключом state
    """
    filter_data = list(filter(lambda x: x.get("state") == state, data))
    return filter_data


def sorted_data(data: List[Dict[str, str]], reverse: Optional[bool] = True) -> List[Dict[str, str]]:
    """
    Функция принимает два аргумента, второй необязательный задает порядок сортировки (убывание, возрастание)
    :return: возвращает новый список, в котором исходные словари отсортированы по убыванию даты (ключ
    date)
    """
    sort_data = sorted(data, key=lambda x: x.get("date"), reverse=reverse)
    return sort_data
