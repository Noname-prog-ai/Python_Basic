# TODO здесь писать код
database = dict()
number_orders = int(input('Введите количество заказов: '))


for number in range(1, number_orders + 1):
  customer, pizza_name, count = input(f'{number} заказ: ').split()
  if customer in database:
    if pizza_name in database[customer]:
      database[customer][pizza_name] += int(count)
    else:
      database[customer][pizza_name] = count
  else:
    database[customer] = dict({pizza_name: int(count)})


for elem_1 in sorted(database):
  print(f'\n{elem_1}:')
  for elem_2 in sorted(database[elem_1]):
    print(f'\t{elem_2}: {database[elem_1][elem_2]}')