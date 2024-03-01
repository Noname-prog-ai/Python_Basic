# TODO здесь писать код
import os

# Получаем абсолютный путь к текущей папке
folder = os.path.abspath(os.path.join('..'))

# Генерируем список путей к файлам внутри папки
gen_files_path = [os.path.join(links, file)
                  for links, dirs, files in os.walk(folder)
                  for file in files]

# Печатаем каждый путь к файлу
for file in gen_files_path:
    print(file)