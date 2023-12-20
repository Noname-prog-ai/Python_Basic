# TODO здесь писать код
letters = "аоиеёэыуюя"
text = input("Введите текст: ")

result = [c for c in text if c in letters]

print("Список гласных букв:", result)
print("Длина списка:", len(result))