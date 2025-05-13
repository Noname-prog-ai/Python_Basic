# TODO здесь писать код
"""Входные данные"""
floats: list[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
names: list[str] = ["vanes", "alen", "jana", "william", "richards", "joy"]
numbers: list[int] = [22, 33, 10, 6894, 11, 2, 1]

"""Создание новых списков"""
new_floats = list(map(lambda x: round(x**3, 3), floats))
new_names = list(filter(lambda x: len(x) >= 5, names))
new_numbers = eval('*'.join(map(str, numbers)))

"""Вывод результатов"""
print(f"Новый список floats: {new_floats}")
print(f"Новый список names: {new_names}")
print(f"Произведение чисел из списка numbers: {new_numbers}")