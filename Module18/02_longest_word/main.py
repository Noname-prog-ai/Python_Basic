# TODO здесь писать код
line = input('Введите строку: '.strip(''))
rus = [chr(i) for i in range(ord('а'),ord('я') + 1)]
total = rus + list(map(lambda x: x.upper(), rus)) + [' ']
only_letters = ''.join(list(filter(lambda x: x in total, line)))
max_len = max(list(map(len, only_letters.split())))
result = [i for i in only_letters.split() if len(i) == max_len][0]
print('Самое длинное слово:', result, '\nДлина этого слова:', max_len, 'символ(ов).')