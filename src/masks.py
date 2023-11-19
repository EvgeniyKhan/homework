import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler = logging.FileHandler("masks.log", mode="w", encoding="utf-8")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def mask_card_number(card_number: str) -> str:
    """
    Функция принимает на вход номер карты и возвращает ее маску
    :rtype: object
    :return: Маска номера карты
    """
    try:
        private_number = card_number[:6] + (len(card_number[6:-4]) * "*") + card_number[-4:]
        chunks, chunk_size = len(private_number), len(private_number) // 4
        mask_number = " ".join([private_number[num:num + chunk_size] for num in range(0, chunks, chunk_size)])
        logger.info(f"Успешно маскирован номер карты пользователя: {mask_number}")
        return mask_number
    except Exception as error:
        logger.error(f"Ошибка при маскировки номера карты: {error}")
        raise


def mask_account_number(account_number: str) -> str:
    """
    Функция принимает на вход номер счёта и возвращает его маску.
    :return: Маска номера счёта
    """
    try:
        private_number = account_number[:6] + (len(account_number[10:-4]) * "*") + account_number[-4:]
        chunks, chunk_size = len(private_number), len(private_number)
        acc_number = " ".join([private_number[num:num + chunk_size] for num in range(10, chunks, chunk_size)])
        logger.info(f"Успешно маскирован номер счета пользователя: {acc_number}")
        return acc_number
    except Exception as error:
        logger.error(f"Ошибка при маскировки номера сета: {error}")
        raise
