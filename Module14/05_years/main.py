# TODO здесь писать код
one = int(input('Введите первый год: '))
two = int(input('Введите второй год: '))
answer = []
for number in range(one, two + 1):
    str_number = str(number)
    set_str_number = set(str_number)
    for digit in set_str_number:
        if str_number.count(digit) > 2:
            answer.append(number)
print(f'Годы от {one} до {two} с тремя одинаковыми цифрами:')
print(*answer, sep='\n')