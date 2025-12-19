from typing import Union


def get_mask_card_number(card_number: Union[int, str]) -> str:
    """Функция, которая частично скрывает номер карты."""
    str_card_number = str(card_number).replace(" ", "")
    if str_card_number.isdigit():
        if len(str_card_number) == 16:
            mask_card_number = str_card_number[0:4] + " " + str_card_number[4:6] + "** **** " + str_card_number[-4:]
            return mask_card_number
        elif len(str_card_number) != 16 and len(str_card_number) != 0:
            return "Недопустимая длина номера карты"
    elif len(str_card_number) == 0:
        return "Номер карты не введён"

    return "Недопустимый формат ввода"


def get_mask_account(account_number: int) -> str:
    """Функция, которая частично скрывает номер счёта."""
    str_account_number = str(account_number).replace(" ", "")
    if str_account_number.isdigit():
        if len(str_account_number) == 20:
            mask_account = "**" + str_account_number[-4:]
            return mask_account
        elif len(str_account_number) != 20 and len(str_account_number) != 0:
            return "Недопустимая длина номера счёта"
    elif len(str_account_number) == 0:
        return "Номер счёта не введён"

    return "Недопустимый формат ввода"
