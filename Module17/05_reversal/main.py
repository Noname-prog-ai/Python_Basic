# TODO здесь писать код
line = input('Введите строку: ')

reversed_flagment = line[line.find('h')+1:line.rfind('h')]
line = reversed_flagment[::-1]

print('Развёреутая последовательность между первым и последним h:', line)