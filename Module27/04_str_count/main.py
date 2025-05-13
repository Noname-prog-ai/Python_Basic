# TODO здесь писать код
import functools


def counter(func):
    """
    Декоратор, который подсчитывает, сколько раз вызывалась оформленная функция.

    Аргументы:
        Функция, которая должна быть оформлена.

    Возвращается:
        Украшенная функция.
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        print(f"Функция '{func.__name__}' была вызвана {wrapper.count} раз")
        return func(*args, **kwargs)

    wrapper.count = 0
    return wrapper


# Example usage
@counter
def greet(name):
    print(f"Здравствуйте, {name}!")


greet("Алиса")
greet("Боб")