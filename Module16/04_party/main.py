guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

# TODO здесь писать код
while True:
    print('Сейчас на вечеринке', len(guests), 'человек:', guests)
    guest = input('Гость пришел или ушел?: ')

    if guest == 'Пора спать':
        print('Вечеринка закончилась, все легли спать')
        break

    name = input('Имя гостя: ')

    if guest == 'пришел':
        if len(guests) < 6:
            guests.append(name)
            print('Привет,', name, '!')
        else:
            print('Прости, ', name, ' но мест нет.', sep="")

    elif guest == 'ушел':
        if name in guests:
            print('Пока,',name)
            guests.remove(name)
        else:
            print('Такого имени нет в списке')