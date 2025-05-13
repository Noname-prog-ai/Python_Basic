# TODO здесь писать код
"""Входные данные"""
letters: list[str] = ['a', 'b', 'c', 'd', 'e']
numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8]


"""
С помощью лямбда-функции создаем кортежи из пар элементов двух списков
Используем list comprehension для преобразования результата в список кортежей
"""
results = [(letters[i], numbers[i]) for i in range(min(len(letters), len(numbers)))]

print(results)