# TODO здесь писать код
from collections import Counter


def can_be_poly(string: str) -> bool:
    """
    Функция проверяет, можно ли получить из данной строки палиндром.

    Аргументы:
    - string: строка, которую нужно проверить

    Возвращает:
    - True, если можно получить палиндром
    - False, если нельзя получить палиндром
    """
    """Создаем словарь с подсчетом количества каждого символа в строке"""
    char_count = Counter(string)

    """Определяем, сколько символов встретилось в нечетном количестве"""
    odd_chars = sum(1 for count in char_count.values() if count % 2 != 0)

    """Если количество символов встретилось нечетное число раз больше одного,
    то невозможно получить палиндром"""
    if odd_chars > 1:
        return False
    else:
        return True


print(can_be_poly('abcba'))  # True
print(can_be_poly('abbbc'))  # False