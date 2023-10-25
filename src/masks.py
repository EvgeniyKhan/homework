def mask_card_number(card_number: str) -> str:
    """
    Функция принимает на вход номер карты и возвращает ее маску
    :rtype: object
    :return: Маска номера карты
    """
    private_number = card_number[:6] + (len(card_number[6:-4]) * "*") + card_number[-4:]
    chunks, chunk_size = len(private_number), len(private_number) // 4
    return " ".join([private_number[num:num + chunk_size] for num in range(0, chunks, chunk_size)])


def mask_account_number(account_number: str) -> str:
    """
    Функция принимает на вход номер счёта и возвращает его маску.
    :return: Маска номера счёта
    """
    private_number = account_number[:6] + (len(account_number[10:-4]) * "*") + account_number[-4:]
    chunks, chunk_size = len(private_number), len(private_number)
    return " ".join([private_number[num:num + chunk_size] for num in range(10, chunks, chunk_size)])
