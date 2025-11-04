def mask_account_card(user_input: str) -> str:
    """Функция, скрывающая номер или счёт карты"""
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
    if len(str_card_number) > 16:
        answer = str_card_name + " " + "**" + str_card_number[-4:]
    else:
        answer = str_card_name + " " + str_card_number[0:4] + " " + str_card_number[
                                                                        4:6] + "** **** " + str_card_number[-4:]

    return answer
