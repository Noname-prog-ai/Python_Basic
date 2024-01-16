# TODO здесь писать код
first_str = list(input('Первая строка: '))
second_str = list(input('Вторая строка: '))
shift = 0

while first_str != second_str:
    second_str.insert(0, second_str.pop())
    shift += 1
    if shift > len(first_str):
        print('Первую строку нельзя получить из второй с помощью циклического сдвига.')
        break
else:
    print(f'Первая строка получается из второй со сдвигом {shift}.')