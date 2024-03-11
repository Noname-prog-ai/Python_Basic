# TODO здесь писать код
import os

class filemanager:

    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        if not os.path.exists(self.filename):
            """создание файла, если он не существует"""
            open(self.filename, 'w').close()
            """открытие файла в режиме записи"""
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        """закрытие файла"""
        self.file.close()
        """подавление всех исключений"""
        return True

    def write_file(self, data):
        """запись данных в файл"""
        self.file.write(data)

    def read_file(self):
        """чтение данных из файла"""
        return self.file.read()


"""При использовании контекст-менеджера FileManager, при попытке открыть несуществующий файл, он будет автоматически создан и открыт в режиме записи. Все исключения, связанные с файлом, будут подавлены при выходе из контекста."""




with filemanager('example.txt') as file:
    file.write_file('hello, world!')

with filemanager('example.txt') as file:
    print(file.read_file())