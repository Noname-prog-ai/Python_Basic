# TODO здесь писать код
while True:
  password = list(input('Придумайте пароль: '))
  length = len(password)
  capital_letters = len(list(filter(lambda x: x.isdigit(), password)))
  numbers = len(list(filter(lambda x: x.isupper(), password)))
  if (length >= 8) and (numbers >= 1) and (capital_letters >= 3):
    print('Это надёжный пароль!')
    break
  else:
    print('Пароль ненадёжный. Попробуйте ещё раз.')