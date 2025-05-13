# TODO здесь писать код
"""Определим функцию-декоратор для проверки прав доступа"""
def check_permission(permission):
    """
    Проверяет наличие прав доступа у пользователя.
    Аргументы:
    - permission (str): право доступа, которое нужно проверить у пользователя
    Returns:
    - wrapper (function): обертка для функции func
    Raises:
    - PermissionError: если у пользователя недостаточно прав для выполнения функции
    """
    def decorator(func):
        """
        Декоратор, добавляющий проверку прав доступа к функции.
        Аргументы:
        - func (function): функция, к которой нужно добавить проверку прав доступа
        Returns:
        - wrapper (function): обертка для функции func
        """
        def wrapper(*args, **kwargs):
            """
            Проверяет наличие прав доступа у пользователя перед выполнением функции.
            Аргументы:
            - args: позиционные аргументы для функции
            - kwargs: именованные аргументы для функции
            Returns:
            - результат выполнения функции func
            Raises:
            - PermissionError: если у пользователя недостаточно прав для выполнения функции
            """
            if permission in user_permissions:
                return func(*args, **kwargs)
            else:
                raise PermissionError(f"У пользователя недостаточно прав, чтобы выполнить функцию {func.__name__}")
        return wrapper
    return decorator

"""Определяем список прав доступа пользователя"""
user_permissions = ['admin']

@check_permission('admin')
def delete_site():
    """
    Удаляет сайт.
    Returns:
    - None
    """
    print('удаляем сайт')

@check_permission('user_1')
def add_comment():
    """
    Добавляет комментарий.
    Returns:
    - None
    """
    print('добавляем комментарий')

"""Вызываем функции"""
delete_site()
add_comment()