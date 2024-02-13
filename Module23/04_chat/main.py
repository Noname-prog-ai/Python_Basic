# TODO здесь писать код
import os

while True:
  try:
    username = input("Введите ваше имя или никнейм: ")
    if username.isalpha():
      break
    else:
      raise ValueError
  except ValueError:
    print("Неправильный ввод! Пожалуйста, убедитесь, что вводите только буквенные символы.\n")

while True:
  print('\n1. Посмотреть текущий текст чата.'
        '\n2. Отправить сообщение.'
        '\n3. Выйти из чата.')
  action_choice = int(input('Выберите действие: '))
  if action_choice == 1:
    try:
      if not os.path.exists('history_chat.txt') or os.stat('history_chat.txt').st_size == 0:
        raise FileNotFoundError
      else:
        with open('history_chat.txt', 'r', encoding='utf-8') as chat_text:
          print(f'\nТекущий текст чата:\n{chat_text.read()}')
    except FileNotFoundError:
      print('--> Чат пуст. Начните общение.')
  elif action_choice == 2:
    try:
      with open('history_chat.txt', 'a', encoding='utf-8') as message_record:
        print(f'\n{username} напишите сообщение:')
        user_message = input('--> ')
        if user_message.strip() == '':
          raise ValueError
        else:
          message_record.write(f'{username}: {user_message}\n')
    except ValueError:
      print('Сообщение не может быть пустой строкой!')
  elif action_choice == 3:
    os.truncate('history_chat.txt', 0)
    break
  else:
    print('Ошибка! Выберите одно из доступных действий.')