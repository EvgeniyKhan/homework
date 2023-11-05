from typing import Dict, Iterator, List


list_transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]


def filter_by_currency(transactions: List[Dict], currency: str) -> Iterator[Dict]:
    """
    Функция фильтрует транзакции по заданной валюте
    :param transactions: Список словарей с транзакциями
    :param currency: Код валюты для фильтрации
    :return: Yield: Dict: Транзакция по заданной валюте
    """
    for transaction in transactions:
        currency_code = transaction["operationAmount"]["currency"]["code"]
        if currency_code == currency:
            yield transaction


def transaction_descriptions(transactions: List[Dict]) -> Iterator[str]:
    """
    Функция возвращает описание каждой операции
    :param transactions: List[Dict] список словарей с транзакциями
    :return: Yield: str: Описание операции
    """
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, end: int) -> Iterator[str]:
    """
    Генератор номеров банковских карт
    :param start: int: Начальное значение для генерации номеров для карт
    :param end: int: Конечное значение для генерации номеров для карт
    :return: Yield: str: номер банковской карты в формате "ХХХХ ХХХХ ХХХХ ХХХХ"
    """
    number_zero = 16 - len(str(end))
    for number in range(start, end + 1):
        number_generator = (number_zero * "0") + str(number)
        yield f'{number_generator[0:4]} {number_generator[4:8]} {number_generator[8:12]} {number_generator[12:17]}'
