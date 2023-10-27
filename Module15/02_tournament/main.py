# TODO здесь писать код
def display_result(participants_names):

    print('Первый день:', participants_names)


def get_participants_names(names):

    names_list = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
    names = []
    for i in range(0, len(names_list) - 1, 2):
        names.append(names_list[i])

    return names


if __name__ == '__main__':
    participants_names = get_participants_names(
        ["Артемий", "Борис", "Влад", "Гоша", "Дима", "Евгений", "Женя", "Захар"]
    )
    display_result(participants_names)