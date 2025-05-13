# TODO здесь писать код
import time

class LoggerDecorator:
    """
    Декоратор для логирования времени выполнения и результатов функции.
    """
    def __init__(self, func):
        """
        Инициализация декоратора.
        Args:
        func (function): Функция для декорирования.
        """
        self.func = func

    def __call__(self, *args, **kwargs):
        """
        Вызывает декорируемую функцию и логирует результаты выполнения.
        Args:
        *args: Позиционные аргументы функции.
        **kwargs: Аргументы функции с ключевыми словами.
        Returns:
        object: Результат выполнения функции.
        """
        start_time = time.time()
        result = self.func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Вызов функции {self.func.__name__}")
        print(f"Аргументы: {args}, {kwargs}")
        print(f"Результат: {result}")
        print(f"Время выполнения: {execution_time} секунд")
        return result

@LoggerDecorator
def complex_algorithm(arg1, arg2):
    # Здесь выполняется сложный алгоритм
    result = 0
    for i in range(arg1):
        for j in range(arg2):
            with open('test.txt', 'w', encoding='utf8') as file:
                file.write(str(i + j))
                result += i + j
    return result


# Пример вызова функции с применением декоратора
result = complex_algorithm(10, 50)