from src.filtration import process_bank_search
from src.utils import get_transactions_from_file
from src.new_format_data_reader import csv_reader, exl_reader
from src.processing import filter_by_state, sort_by_date
from src.generators import filter_by_currency

def main():
    while True:
        print("""Программа: Привет! Добро пожаловать в программу работы с банковскими транзакциями.
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла
""")

        user_input = input("Пользователь: ")

        if user_input == "1":
            get_info = get_transactions_from_file("data/operations.json")
            print("Программа: Для обработки выбран JSON-файл.")
            break
        elif user_input == "2":
            get_info = csv_reader("data/transactions.csv")
            print("Программа: Для обработки выбран CSV-файл.")
            break
        elif user_input == "3":
            get_info = exl_reader("data/transactions_excel.xlsx")
            print("Программа: Для обработки выбран XLSX-файл.")
            break
        else:
            print("Программа: Неверный пункт меню. Попробуйте ещё раз.")

    print(get_info)

    while True:
        print("""Программа: Введите статус, по которому необходимо выполнить фильтрацию. 
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING""")
        status_choice = input("Пользователь: ").upper()
        if status_choice == "EXECUTED":
            filtered_transactions = filter_by_state(get_info)
            break
        elif status_choice == "CANCELED":
            filtered_transactions = filter_by_state(get_info, "CANCELED")
            break
        elif status_choice == "PENDING":
            filtered_transactions = filter_by_state(get_info, "PENDING")
            break
        else:
            print("Программа: Неверный пункт меню. Попробуйте ещё раз.")

    print(filtered_transactions)

    while True:
        print("""Программа: Отсортировать операции по дате? Да/Нет""")
        data_choice = input("Пользователь: ").upper()
        if data_choice == "НЕТ":
            sorted_by_date = filtered_transactions
            break
        elif data_choice == "ДА":
            print("""Отсортировать по возрастанию или по убыванию?""")
            sort_choice = input("Пользователь: ").lower()
            if sort_choice == "по убыванию":
                sorted_by_date = sort_by_date(filtered_transactions)
                break
            elif sort_choice == "по возрастанию":
                sorted_by_date = sort_by_date(filtered_transactions, False)
                break
            else:
                print("Программа: Неверный пункт меню. Попробуйте ещё раз.")
        else:
            print("Программа: Неверный пункт меню. Попробуйте ещё раз.")

    print(sorted_by_date)

    while True:
        print("""Программа: Выводить только рублевые транзакции? Да/Нет""")
        currency_choice = input("Пользователь: ").upper()
        if currency_choice == "НЕТ":
            sorted_by_currency = sorted_by_date
            break
        elif currency_choice == "ДА":
            sorted_by_currency = filter_by_currency(sorted_by_date, "RUB")
            break
        else:
            print("Программа: Неверный пункт меню. Попробуйте ещё раз.")

    print(sorted_by_currency)

    while True:
        print("""Программа: Отфильтровать список транзакций по определенному слову в описании? Да/Нет""")
        filter_choice = input("Пользователь: ").upper()
        if filter_choice == "НЕТ":
            sorted_by_filter = sorted_by_currency
            break
        elif filter_choice == "ДА":
            user_search = input("Введите слово для поиска: ")
            sorted_by_filter = process_bank_search(sorted_by_currency, user_search)
            break
        else:
            print("Программа: Неверный пункт меню. Попробуйте ещё раз.")

    print(sorted_by_filter)

    print("Программа: Распечатываю итоговый список транзакций...")

    if sorted_by_filter:
        print(f"Программа: Всего банковских операций в выборке: {len(list(sorted_by_filter))}")
        for operations in sorted_by_filter:
            print(operations)
    else:
        print("Программа: Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")




if __name__ == "__main__":

    main()
