import pytest
from src.widget import card_information, format_date


@pytest.mark.parametrize("input_numb, expected_output", [
                        ("Visa Platinum 7000792289606361",
                         "Visa Platinum 7000 79** **** 6361"),
                        ("Счет 73654108430135874305",
                         "Счет **4305")
])
def test_card_information(input_numb, expected_output):
    assert card_information(input_numb) == expected_output


@pytest.mark.parametrize("input_data, expected_output", [
                        ("2018-07-11T02:26:18.671407",
                         "11.07.2018")
])
def test_format_date(input_data, expected_output):
    assert format_date(input_data) == expected_output
