# TODO здесь писать код
site = {
'html': {
'head': {
'title': 'Мой сайт'
},
'body': {
'h2': 'Здесь будет мой заголовок',
'div': 'Тут, наверное, какой-то блок',
'p': 'А вот здесь новый абзац'
}
}
}

def search_key(key, data, depth=0):
  res = None
  if key in data:
    return data[key]
  if depth - 1:
    for value in data.values():
      if isinstance(value, dict):
        res = search_key(key, value, depth - 1)
        if res:
          return res
  return res


key = input('Введите искомый ключ: ')
yes_no = input('Хотите ввести максимальную глубину? Y/N: ').lower()
if yes_no == 'y':
  depth = int(input('Введите максимальную глубину: '))
  print(f'Значение ключа: {search_key(key, site, depth)}')
elif yes_no == 'n':
  print(f'Значение ключа: {search_key(key, site)}')
else:
  print('Ошибка ввода.')