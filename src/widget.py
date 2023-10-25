from src.masks import mask_card_number, mask_account_number


def card_information(type_and_number: str | list[str], account_number: str) -> str:
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

print(card_information("Visa 1234123412341234", "Счёт 12341234123412341234"))