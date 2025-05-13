# TODO здесь писать код
# Создаем класс MyDict и наследуем его от класса dict
class MyDict(dict):
    # Переопределяем метод get
    def get(self, key, default=None):
        # Если ключ есть в словаре, возвращаем его значение
        if key in self:
            return self[key]
        # Если ключа нет в словаре, возвращаем число 0
        else:
            return 0

# Пример использования
my_dict = MyDict({'a': 1, 'b': 2, 'c': 3})
print(my_dict.get('a'))  # Вывод: 1
print(my_dict.get('d'))  # Вывод: 0