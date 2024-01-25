# TODO здесь писать код
database = dict()
number_orders = int(input('Введите количество заказов: '))
for number in range(1, number_orders + 1):
  order = input(f'{number} заказ: ').split()
  if order[0] in database:
    if order[1] in database[order[0]]:
      database[order[0]][order[1]] += int(order[2])
    else:
      database[order[0]][order[1]] = order[2]
  else:
    database[order[0]] = dict({order[1]: int(order[2])})
for elem_1 in sorted(database):
  print(f'\n{elem_1}:')
  for elem_2 in sorted(database[elem_1]):
    print(f'\t{elem_2}: {database[elem_1][elem_2]}')