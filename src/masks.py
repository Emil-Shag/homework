from typing import Union
import logging


logger = logging.getLogger('masks')
logger.setLevel(logging.DEBUG)


file_handler = logging.FileHandler('logs/masks.log', mode='w', encoding="utf-8")
file_handler.setLevel(logging.DEBUG)


file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)


logger.addHandler(file_handler)


def get_mask_card_number(card_number: Union[int, str]) -> str:
    """Функция, которая частично скрывает номер карты."""
    str_card_number = str(card_number).replace(" ", "")
    if str_card_number.isdigit():
        if len(str_card_number) == 16:
            mask_card_number = str_card_number[0:4] + " " + str_card_number[4:6] + "** **** " + str_card_number[-4:]
            logger.info(f"Маска карты успешно создана: {mask_card_number}")
            return mask_card_number
        elif len(str_card_number) != 16 and len(str_card_number) != 0:
            logger.error("Ошибка: Номер карты должен содержать 16 цифр.")
            return "Недопустимая длина номера карты"
    elif len(str_card_number) == 0:
        logger.error("Ошибка: Номер карты должен содержать 16 цифр.")
        return "Номер карты не введён"
    logger.error("Ошибка: Номер карты должен состоять из цифр.")
    return "Недопустимый формат ввода"


def get_mask_account(account_number: int) -> str:
    """Функция, которая частично скрывает номер счёта."""
    str_account_number = str(account_number).replace(" ", "")
    if str_account_number.isdigit():
        if len(str_account_number) == 20:
            mask_account = "**" + str_account_number[-4:]
            logger.info(f"Маска счета успешно создана: {mask_account}")
            return mask_account
        elif len(str_account_number) != 20 and len(str_account_number) != 0:
            logger.error("Ошибка: Номер счета должен содержать 20 цифр.")
            return "Недопустимая длина номера счёта"
    elif len(str_account_number) == 0:
        logger.error("Ошибка: Номер счета должен содержать 20 цифр.")
        return "Номер счёта не введён"
    logger.error("Ошибка: Номер карты должен состоять из цифр.")
    return "Недопустимый формат ввода"
