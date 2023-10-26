from src.masks import mask_card_number, mask_account_number


def card_information(masking: str) -> str:
    """
    Принимает на вход строку информацией тип карты/счета и номер карты/счета
    :return: Возвращает эту строку с замаскированным номером карты/счета.
    """
    list_mask = masking.split()
    join_mask = ' '.join(list_mask[:-1])

    if 'счет' == list_mask[0].lower():
        return f'{join_mask} {mask_account_number(list_mask[-1])}'
    return f'{join_mask} {mask_card_number(list_mask[-1])}'


def format_date(input_date: str) -> str:
    """
    Функция, которая принимает на вход строку, вида "2018-07-11T02:26:18.671407"
    :return: возвращает строку с датой в виде "11.07.2018"
    """
    formatted_date = input_date.split('T')[0]
    year, month, day = formatted_date.split('-')
    return f"{day}.{month}.{year}"
