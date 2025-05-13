# TODO здесь писать код
def capitalize(line):
  return ' '.join([line.capitalize() for line in line.split()])
line = input('Введите строку: ')
print('Результат:', capitalize(line))