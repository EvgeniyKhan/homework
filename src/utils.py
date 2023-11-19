import json
import os
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler = logging.FileHandler("utils.log", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def load_transactions(file_path):
    """
    Запуск данных о финансовых транзакциях из JSON файла
    :param file_path: Путь к JSON файлу с данными о транзакциях
    :return: Список словарей с данными
    """
    if not os.path.exists(file_path):
        print(f"Файл {file_path} не найден!")
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, list):
            logger.error(f"Файл {file_path} не содержит список транзакций")
            return []

        return data
    except FileNotFoundError as error:
        logger.error(f"Файл {file_path} не найден: {error}")
        return []

    except json.JSONDecodeError as error:
        logger.error(f"Ошибка при декодировании JSON в файле{file_path}: {error}")
        return []


def convert_to_rubles(transaction):
    """
    Конвертирует сумму транзакции в рубли, если транзакция совершена в другой валюте
    :param transaction: Словарь с данными о транзакции, включая сумма транзакции
    :return: Сумма транзакции в рублях (float) или ошибка ValueError
    """
    amount = transaction.get("amount")
    currency = transaction.get("currency")

    if amount is None:
        logger.error("Транзакция не содержит 'amount'")
        raise ValueError("Транзакция не содержит 'amount'")

    if currency == "RUB":
        return float(amount)
    else:
        logger.error("Транзакция выполнена не в рублях. Укажите транзакцию в рублях")
        raise ValueError("Транзакция выполнена не в рублях. Укажите транзакцию в рублях")
