# TODO здесь писать код
"""Импортируем модуль os для работы с операционной системой и модуль _collections_abc для импорта класса Iterator."""
import os
from _collections_abc import Iterator


"""Создаем функцию gen_files_path, которая является генератором файловых путей в заданной директории и ее поддиректориях. Она принимает два параметра: user_file - название файла или папки, которую нужно найти, path - путь к директории, по умолчанию текущая директория."""
def gen_files_path(user_file: str, path=None) -> Iterator:
    """
    Генератор файловых путей в заданной директории и ее поддиректориях
    :param user_file: название файла или папки, которую нужно найти
    :param path: путь к директории, по умолчанию текущая директория
    :return: генератор файловых путей
    """
    """Затем определяемфункцию gen_files_path.Внутри этой функции, если не указан путь к директории(path is None), то os.path.abspath(os.path.sep) возвращает абсолютный путь до корневой директории операционной системы."""
    if path is None:
        path = os.path.abspath(os.path.sep)

    print(f'директория поиска: {path}\n')

    """Далее происходит обход директории и поддиректорий с помощью функции os.walk.Мы выводим информацию о поиске - где ищем(папки или файлы) и выводим пути."""
    for root, dirs, files in os.walk(path):
        print('\nпоиск идет в папках директории')
        for i_dir in dirs:
            yield os.path.join(root, i_dir)

        print('\nпоиск идет в файлах директории')
        for i_file in files:
            yield os.path.join(root, i_file)

        """Затем проверяем, если user_file в списке dirs, то выводим сообщение, что папка найдена, иначе если user_file в списке files, то выводим сообщение, что файл найден.Если файл не найден ни в dirs, ни в files, то возникает исключение FileNotFoundError с соответствующим сообщением."""
        try:
            if user_file in dirs:
                return print(f'\nпапка {user_file} находится в директории')
            elif user_file in files:
                return print(f'\nфайл {user_file} находится в директории')
            raise FileNotFoundError(f'\nв данной директории нет файла {user_file}')
        except FileNotFoundError as exc:
            return print(exc)


def main():
    name_file = 'get-pip.py'

    """В функции main мы просто вызываем gen_files_path, передавая в качестве аргумента name_file. Затем выводим все найденные пути."""
    for name in gen_files_path(name_file):
        print(name)


main()