import pandas as pd
import csv


def read_csv(file_path):
    """
    Читает данные из файла csv о финансовых операционных транзакций.
    :param file_path: Путь к файлу csv
    :return: Возвращает, список транзакций из файла csv
    """
    transactions = []
    with open(file_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=";")
        for row in reader:
            transactions.append(row)
    return transactions


def read_xlsx(file_path):
    """
    Преобразовывает данные из файла xlsx в список транзакций.
    :param file_path: Путь к файлу xlsx
    :return: Возвращает, список транзакций из файла xlsx
    """
    df = pd.read_excel(file_path)
    transactions = df.to_dict("records")
    return transactions
