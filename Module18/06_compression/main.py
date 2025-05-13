# TODO здесь писать код
def compression(text):
  counter = 1
  compressed = []
  for i in range(len(text)):
    if text[i] == text[i + 1: i + 2]:
      counter += 1
      continue
    compressed.append(text[i] + str(counter))
    counter = 1
  return compressed
plain_text = input('Введите строку: ')
print('Закодированная строка: {}'.format(''.join(compression(plain_text))))