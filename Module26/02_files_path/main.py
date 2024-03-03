# TODO здесь писать код
"""Импортируем модуль os"""
import os

"""Получаем абсолютный путь до папки выше текущей"""
folder = os.path.abspath(os.path.join('..'))

"""Генерируем список путей до всех файлов внутри папки и подпапок"""
gen_files_path = [os.path.join(links, file)
                  for links, dirs, files in os.walk(folder)
                  for file in files]

"""Выводим каждый полученный путь"""
for file in gen_files_path:
    print(file)