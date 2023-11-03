import pytest
from src.masks import mask_card_number, mask_account_number


@pytest.mark.parametrize("input_card, expected_output", [
                        ("7000792289606361",
                         "7000 79** **** 6361")
])
def test_mask_card_number(input_card, expected_output):
    assert mask_card_number(input_card) == expected_output


@pytest.mark.parametrize("input_number, expected", [
                        ("73654108430135874305",
                         "**4305")
])
def test_mask_account_number(input_number, expected):
    assert mask_account_number(input_number) == expected
