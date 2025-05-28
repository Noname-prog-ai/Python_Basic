# TODO здесь писать код

# Список чисел для работы (итоговый алгоритм проверьте на разных списках, придуманных самостоятельно):
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8]

pnumbers_list = (numbers_list[::-1])

print('Четные числа в обратном порядке: ')
for number in pnumbers_list:
  if number % 2 == 0:
    print(number, end=' ')
