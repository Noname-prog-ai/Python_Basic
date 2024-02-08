# TODO здесь писать код
import os
def count_files_dirs_size(path):
    size = 0
    files = 0
    dirs = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            size += os.path.getsize(fp)
            files += 1
        dirs += len(dirnames)
    return (files, dirs, size)


path = input("Введите путь до каталога: ")
(files, dirs, size) = count_files_dirs_size(path)

print("Размер каталога (в Кб):", size/1024)
print("Количество подкаталогов:", dirs)
print("Количество файлов:", files)