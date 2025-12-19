from datetime import datetime


def log(filename=None):
    """Декоратор для записи времени выполнения функции и записи результатов в файл"""

    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                time_1 = datetime.now()
                result = func(*args, **kwargs)
                time_2 = datetime.now()
                log_text = f"{func.__name__} ok, start time func: {time_1}, finish time func: {time_2}"
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(log_text)
                else:
                    print(log_text)
                return result
            except Exception as e:
                log_text = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}"
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(log_text)
                else:
                    print(log_text)
                raise

        return wrapper

    return decorator
