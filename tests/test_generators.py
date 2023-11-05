from src.generators import filter_by_currency, transaction_descriptions, card_number_generator, list_transactions


def test_filter_by_currency():
    usd_transactions = list(filter_by_currency(list_transactions, "USD"))
    assert len(usd_transactions) == 3
    assert usd_transactions[0]["id"] == 939719570
    assert usd_transactions[1]["id"] == 142264268


def test_transaction_description():
    description = list(transaction_descriptions(list_transactions))
    assert len(description) == 5
    assert description[0] == "Перевод организации"
    assert description[1] == "Перевод со счета на счет"
    assert description[2] == "Перевод со счета на счет"
    assert description[3] == "Перевод с карты на карту"
    assert description[4] == "Перевод организации"


def test_card_number_generator():
    card_number = list(card_number_generator(1, 5))
    assert len(card_number) == 5
    assert card_number[0] == "0000 0000 0000 0001"
    assert card_number[1] == "0000 0000 0000 0002"
    assert card_number[2] == "0000 0000 0000 0003"
    assert card_number[3] == "0000 0000 0000 0004"
    assert card_number[4] == "0000 0000 0000 0005"
