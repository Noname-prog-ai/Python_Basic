text = """ Lorem ipsum dolor sit amet, consectetuer adipiscing elit. 
Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, 
nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. 
Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate 
"""

# TODO здесь писать код
import re
"""Поиск всех слов, состоящих из четырех букв"""
words = re.findall(r'\b\w{4}\b', text)

"""Вывод результата"""
print(words)