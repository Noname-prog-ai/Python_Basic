# TODO здесь писать код
import collections

text = input('Введите текст: ').lower()
vocabulary = dict()
sym_dict = dict()
print('Оригинальный словарь частот:')

for sym in text:
    sym_dict[sym] = sym_dict.get(sym, 0) + 1

for i_sym in sorted(sym_dict.keys()):
    print(i_sym, ':', sym_dict[i_sym])

for letter, serial_num in collections.Counter(text).items():
    vocabulary.setdefault(serial_num, []).append(letter)
print('\nИнвертированный словарь частот:')

for i_vocabulary in vocabulary:
    print(i_vocabulary, vocabulary[i_vocabulary])
