# TODO здесь писать код
def singleton(cls):
    """Словарь для хранения экземпляров класса"""
    instances = {}

    """Вложенная функция для проверки существования экземпляра и его создания"""
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


"""Применяем декоратор к классу"""
@singleton
class Example:
     pass

"""Создаем первый экземпляр класса Example"""
my_obj = Example()

"""Создаем второй экземпляр класса Example"""
my_another_obj = Example()

"""Выводим идентификаторы обоих экземпляров"""
print(id(my_obj))
print(id(my_another_obj))

"""Проверяем, являются ли оба экземпляра одним и тем же объектом"""
print(my_obj is my_another_obj)