# TODO здесь писать код
line = input('Введите строку: ')
a = set()
for i in line:
  if i in a:
    a.remove(i)
  else:
    a.add(i)
print(('Можно','Нельзя')[len(a)>1], 'сделать полиндром')