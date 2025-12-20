from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(user_input: str) -> str:
    """Функция, скрывающая номер или счёт карты"""
    if not user_input:
        return "Некорректный ввод данных"
    input_parts = user_input.split()
    card_name = []
    card_number = []
    for part in input_parts:
        if part.isalpha():
            card_name.append(part)
        elif part.isdigit():
            card_number.append(part)
    str_card_name = " ".join(card_name)
    str_card_number = " ".join(card_number)
    if len(str_card_number) == 20:
        answer = str_card_name + " " + get_mask_account(int(str_card_number))
    elif len(str_card_number) == 16:
        answer = str_card_name + " " + get_mask_card_number(int(str_card_number))
    else:
        answer = "Некорректный ввод данных"

    return answer


def get_date(iso_format_date: str) -> str:
    """Функция, преобразующая строку с датой из одного формата в другой"""
    new_format_date = iso_format_date[8:10]
    new_format_month = iso_format_date[5:7]
    new_format_year = iso_format_date[0:4]
    check_digit = new_format_date + new_format_month + new_format_year
    if (
        check_digit.isdigit()
        and 1 <= int(new_format_date) <= 31
        and 1 <= int(new_format_month) <= 12
        and 1 <= int(new_format_year) <= 2025
    ):
        required_date_format = new_format_date + "." + new_format_month + "." + new_format_year
        return required_date_format
    else:
        return "Неверно указаны параметры даты"
