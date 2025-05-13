# TODO здесь писать код
import functools
from datetime import datetime


def logging_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """Вывод названия функции и ее документации"""
        print(f"Название функции: {func.__name__}")
        print(f"Функциональная документация: {func.__doc__}")

        try:
            return func(*args, **kwargs)
        except Exception as e:
            """Запись ошибки в файл"""
            with open("function_errors.log", "a") as file:
                file.write(f"[{datetime.now()}] Function name: {func.__name__}, Error: {str(e)}\n")

    return wrapper

@logging_decorator
def divide(a: float, b: float) -> float:
    """
    Эта функция делит два числа.
    """
    return a / b

@logging_decorator
def multiply(a: float, b: float) -> float:
    """
    Эта функция умножает два числа.
    """
    return a * b

@logging_decorator
def subtract(a: float, b: float) -> float:
    """
    Эта функция вычитает второе число из первого.
    """
    return a - b

"""Вызов функций"""
print(divide(10, 2))
print(multiply(5, 5))
print(subtract(8, 3))