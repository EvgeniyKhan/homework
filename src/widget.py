from src.masks import mask_card_number, mask_account_number


def card_information(type_and_number: str | list[str], account_number) -> str:
    """
    Принимает на вход строку информацией тип карты/счета и номер карты/счета
    :param type_and_number:
    :param account_number:
    :return: Возвращает эту строку с замаскированным номером карты/счета.
    """
    split_list = type_and_number.split()
    split_account = account_number.split()
    account = mask_account_number(split_account[-1])
    numbers_account = split_account[:1]
    one_line = ''.join(numbers_account)
    if len(split_list) == 3:
        only_number = mask_card_number(split_list[-1])
        only_type = split_list[:2]
        only_card_number = ' '.join(only_type)
        return f'{only_card_number} {only_number} \n{one_line} {account}'
    elif len(split_list) == 2:
        only_number = mask_card_number(split_list[-1])
        only_type = split_list[:1]
        only_card_number = ' '.join(only_type)
        return f'{only_card_number} {only_number} \n{one_line} {account}'
    else:
        return 'Не верно введён номер карты или счёта'


def input_date(date: str) -> str:
    """
    Функция принимает на вход дату и время
    :param date: дату и время
    :return: Возвращает дату ДД.ММ.ГГГГ
    """
    return f"{date[8:10]}.{date[5:7]}.{date[:4]}"
