from src.new_format_data_reader import csv_reader, exl_reader

if __name__ == "__main__":

    print(csv_reader("data/transactions.csv"))
    print(exl_reader("data/transactions_excel.xlsx"))
