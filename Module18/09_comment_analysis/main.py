# TODO здесь писать код
def count_uppercase_lowercase(text):
  uppercase = sum(1 for i in text if i.isupper())
  lowercase = sum(1 for i in text if i.islower())
  return uppercase, lowercase


# Пример использования:
text = input("Введите строку для анализа: ")
uppercase, lowercase = count_uppercase_lowercase(text)
print("Количество заглавных букв:", uppercase)
print("Количество строчных букв:", lowercase)
