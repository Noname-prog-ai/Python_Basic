# TODO здесь писать код
"""Задаем функцию count_unique_characters, которая принимает строку message в качестве аргумента"""
def count_unique_characters(message):
    """Преобразуем все символы строки в нижний регистр, чтобы алгоритм был регистронезависимым"""
    message = message.lower()
    """Используем lambda-функцию, map и filter для получения списка уникальных символов в строке"""
    unique_characters = list(filter(lambda x: message.count(x) == 1, message))
    """Возвращаем количество уникальных символов в строке"""
    return len(unique_characters)

"""Задаем строку message, содержащую загадочное письмо с шифровкой"""
message = "today is a beautiful day! the sun is shining and the birds are singing."
"""Вызываем функцию count_unique_characters и передаем ей строку message"""
unique_count = count_unique_characters(message)


# Пример использования:
message = "Today is a beautiful day! The sun is shining and the birds are singing."

unique_count = count_unique_characters(message)
print("Количество уникальных символов в строке:", unique_count)
