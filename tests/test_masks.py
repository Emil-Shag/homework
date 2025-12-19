import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, mask_card_number",
    [
        (7000792289606361, "7000 79** **** 6361"),
        (32145345098, "Недопустимая длина номера карты"),
        ("", "Номер карты не введён"),
        ("7000 7922 8960 6361", "7000 79** **** 6361"),
        ("qwertyuiasdfghjk", "Недопустимый формат ввода"),
    ],
)
def test_mask_number(card_number, mask_card_number):
    assert get_mask_card_number(card_number) == mask_card_number


@pytest.mark.parametrize(
    "card_account, mask_card_account",
    [
        (73654108430135874305, "**4305"),
        (736541084301, "Недопустимая длина номера счёта"),
        ("", "Номер счёта не введён"),
        ("7365 410 84301 358 743 05", "**4305"),
        ("qwertyuiasdfghjk", "Недопустимый формат ввода"),
    ],
)
def test_mask_account(card_account, mask_card_account):
    assert get_mask_account(card_account) == mask_card_account
