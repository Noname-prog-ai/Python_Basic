goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# TODO здесь писать код
for item in goods.keys():
  total_price = 0
  total_count = 0
  for i_list in range(len(store[goods[item]])):
    total_price += store[goods[item]][i_list]['quantity'] * store[goods[item]][i_list]['price']
    total_count += store[goods[item]][i_list]['quantity']
  print(f'{item} - {total_count} шт, стоимость {total_price} руб')
