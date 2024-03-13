# TODO здесь писать код
"""Импорт необходимого модуля"""
import datetime

"""Создание декоратора"""
def log_methods(date_format: str):
    def decorator(cls):
        class decoratedclass(cls):
            def __getattribute__(self, name):
                attr = super().__getattribute__(name)
                if callable(attr) and not name.startswith('__'):
                    def wrapper(*args, **kwargs):
                        start_time = datetime.datetime.now()
                        print(f"запускается '{cls.__name__}.{name}'. дата и время запуска: {start_time.strftime(date_format)}.")
                        result = attr(*args, **kwargs)
                        end_time = datetime.datetime.now()
                        execution_time = end_time - start_time
                        print(f"завершение '{cls.__name__}.{name}', время работы = {execution_time.total_seconds()} s.")
                        return result
                    return wrapper
                return attr
        return decoratedclass
    return decorator

"""Применение декоратора к классу"""
@log_methods("March 13 2024 — 19:15:37")
class a:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result

"""Наследование и применение декоратора к классу-наследнику"""
@log_methods("March 13 2024 — 19:15:37")
class b(a):
    def test_sum_1(self):
        super().test_sum_1()
        print("наследник test sum 1")

    def test_sum_2(self):
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result

"""Создание объекта класса b"""
my_obj = b()

"""Вызов методов объекта с выводом информации о времени выполнения"""
my_obj.test_sum_1()
my_obj.test_sum_2()
