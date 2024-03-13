# TODO здесь писать код
"""Создаем декоратор decorator_with_args_for_any_decorator"""
def decorator_with_args_for_any_decorator(*dec_args, **dec_kwargs):
    """Создаем декоратор decorated_decorator, который будет принимать другую функцию-декоратор с произвольными аргументами"""
    def decorated_decorator(func):
        """Создаем новую функцию-декоратор, которая будет принимать аргументы и ключевые аргументы"""
        def wrapper(*args, **kwargs):
            """Выводим переданные аргументы и ключевые аргументы в декоратор"""
            print("Переданные арги и кварги в декоратор:", dec_args, dec_kwargs)
            """Вызываем исходную функцию-декоратор и передаем в нее аргументы и ключевые аргументы"""
            func(*args, **kwargs)

        """Возвращаем новую функцию-декоратор"""
        return wrapper

    """Возвращаем декоратор decorated_decorator"""
    return decorated_decorator


"""Используем декоратор decorator_with_args_for_any_decorator"""
@decorator_with_args_for_any_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)


"""Вызываем декорированную функцию"""
decorated_function("юзер", 101)
