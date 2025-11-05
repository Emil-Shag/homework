def get_mask_card_number(card_number: int) -> str:
    """Функция, которая частично скрывает номер карты."""
    str_card_number = str(card_number)
    mask_card_number = str_card_number[0:4] + " " + str_card_number[4:6] + "** **** " + str_card_number[-4:]
    return mask_card_number


def get_mask_account(account_number: int) -> str:
    """Функция, которая частично скрывает номер счёта."""
    str_account_number = str(account_number)
    mask_account = "**" + str_account_number[-4:]
    return mask_account
