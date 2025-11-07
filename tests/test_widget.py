import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "account_num, mask_account_num",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("MasterCard 5185373029202738", "MasterCard 5185 37** **** 2738"),
        ("Счет 12345678901234567890", "Счет **7890"),
        ("QWERTY", "Некорректный ввод данных"),
        ("", "Некорректный ввод данных"),
        ("123", "Некорректный ввод данных"),
    ],
)
def test_mask_account_card(account_num, mask_account_num):
    assert mask_account_card(account_num) == mask_account_num


@pytest.mark.parametrize(
    "iso_format, new_format",
    [
        ("2019-07-03T18:35:29.512364", "03.07.2019"),
        ("2018-06-30T02:08:58.425572", "30.06.2018"),
        ("2020-100-66T18:35:29.512364", "Неверно указаны параметры даты"),
        ("/@334$%%^", "Неверно указаны параметры даты"),
        ("", "Неверно указаны параметры даты"),
    ],
)
def test_get_date(iso_format, new_format):
    assert get_date(iso_format) == new_format
