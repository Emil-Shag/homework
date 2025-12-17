from time import time


def log(filename = None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            time_1 = time()
            result = func(*args, **kwargs)
            time_2 = time()
            log_text = f'{func.__name__} ok, start time func: {time_1}, finish time func: {time_2}'
            if filename:
                with open(filename, "a", encoding="utf-8") as file:
                    file.write(log_text)
            else:
                print(log_text)
            return result

        return wrapper
    return decorator
