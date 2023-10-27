# TODO здесь писать код

# Список чисел для работы (итоговый алгоритм проверьте на разных списках, придуманных самостоятельно):
numbers_list = [7, 14, 3, 18, 21, 10, 9, 6]
arr = numbers_list
print('Исходный список:', numbers_list)

n = len(arr)
for i in range(n - 1):
    for j in range(n - i - 1):
        if arr[j] < arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print('Отсортированный список четных чисел:', [n for n in arr if n % 2 == 0])
