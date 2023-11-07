# TODO здесь писать код
def display_result(participants_names):
  print('Первый день:', participants_names)


def get_participants_names(names_list):
  names = []
  for i in range(0, len(names_list) - 1, 2):
    names.append(names_list[i])

  return names


if __name__ == '__main__':
  names_list = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
  participants_names = get_participants_names(names_list)
  display_result(participants_names)