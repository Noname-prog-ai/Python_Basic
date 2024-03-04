# TODO здесь писать код
import os
from collections.abc import Iterable


"""Функция strings_count принимает аргумент directory, который указывает на путь к директории, и возвращает генератор из кортежей."""
"""Каждый кортеж содержит путь к файлу и количество строк кода в файле."""
def strings_count(directory: str) -> Iterable[tuple]:
    """
    Функция для подсчета количества строк кода в файлах с расширением .py в указанной директории и всех ее поддиректориях.
    :param directory: путь к директории
    :return: генератор из кортежей (путь к файлу, количество строк кода)
    """
    """Обход всех поддиректорий и файлов в указанной директории"""
    for root, dirs, files in os.walk(directory):
        for file in files:
            count = 0
            """Проверяем, является ли файл файлом с расширением .py"""
            if os.path.join(root, file).endswith('.py'):
                curr_file = open(os.path.join(root, file), 'r', encoding='utf-8')
                """Подсчет количества строк кода в файле"""
                for line in curr_file.readlines():
                    """Условие для исключения пустых строк и строк, начинающихся с комментариев"""
                    if not (line == '\n' or line.strip().startswith(('"', '#', "'"))):
                        count += 1
                """Возвращаем путь к файлу и количество строк кода в файле с помощью yield"""
                yield os.path.join(root, file), count


"""Пример использования функции strings_count"""
for element in strings_count(directory='..'):
    print('Файл "{}": строк кода - {}'.format(element[0], element[1]))