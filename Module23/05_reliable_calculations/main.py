# TODO здесь писать код

# Здесь создайте функцию get_sage_sqrt
from math import sqrt


def get_sage_sqrt(num):
    try:
        if isinstance(num, (int, float)):
            if num < 0:
                raise ValueError('число должно быть положительным')
            elif num == 0:
                raise ZeroDivisionError('у нуля нет корня.')
            else:
                res = sqrt(num)
                str_num = str(res)
                if '.' in str_num[-2]:
                    return int(res)
                else:
                    return res
        else:
            raise TypeError('ожидали число получили строку')
    except (ValueError, ZeroDivisionError, TypeError) as exc:
        return exc

# Тестовые случаи
numbers = [16, 25, -9, 0, 4.5, "abc"]
for number in numbers:
    result = get_sage_sqrt(number)
    print(f"Квадратный корень numbers {number}: {result}")