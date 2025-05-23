# TODO здесь писать код
"""Создаем функцию-декоратор"""
def cache_results(func):
    """Создаем словарь для хранения результатов"""
    cache = {}

    """Создаем функцию-обертку"""
    def wrapper(number):
        """Проверяем, есть ли результат в кэше"""
        if number in cache:
            """Если есть, возвращаем его"""
            return cache[number]
        else:
            """Если нет, вычисляем результат"""
            result = func(number)
            """Сохраняем результат в кэше"""
            cache[number] = result
            """Возвращаем результат"""
            return result

    """Возвращаем функцию-обертку в качестве декорированной функции"""
    return wrapper


def fibonacci(number):
    if number <= 1:
        return number
    return fibonacci(number - 1) + fibonacci(number - 2)


# Вычисление числа Фибоначчи с использованием кеширования
print(fibonacci(10))  # Результат будет кеширован

# Повторное вычисление числа Фибоначчи с теми же аргументами
print(fibonacci(10))  # Результат будет взят из кеша

# Вычисление числа Фибоначчи с другим аргументом
print(fibonacci(5))  # Результат будет вычислен и закеширован
