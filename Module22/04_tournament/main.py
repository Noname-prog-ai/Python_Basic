# TODO здесь писать код
import os

text_first_tour = ['80', 'Ivanov Serg 80', 'Sergeev Petr 92',
                   'Petrov Vasiliy 98', 'Vasiliev Maxim 78']
with open('first_tour.txt', 'w') as new_file_one:
    for line in text_first_tour:
        new_file_one.write(line + '\n')

number_of_scores = []
with open('first_tour.txt', 'r') as read_line_add_in_list:
    k = int(read_line_add_in_list.readline())
    for line in read_line_add_in_list:
        new_line = line.split()
        if int(new_line[-1]) > k:
            number_of_scores.append(new_line)

number_of_scores.sort(key=lambda a: int(a[-1]))
number_of_scores.reverse()
with open("first_tour.txt", 'r') as fin:
    k = int(next(fin))
    ps = sorted(((int(sc), fn[0], ln) for ln, fn, sc in map(str.split, fin) if int(sc) > k), reverse=True)

with open("second_tour.txt", 'w') as fout:
    print(len(ps), '\n'.join(f"{i}) {fn}. {ln} {sc}" for i, (sc, fn, ln) in enumerate(ps, 1)), file=fout, sep='\n')
