films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']

# TODO здесь писать код
def choose_movies(arr):
    res = []
    n = int(input('Сколько фильмов хотите добавить?: '))
    for _ in range(n):
        name = input('Введите название фильма: ')
        if name in arr:
            res.append(name)
        else:
            print(f'Ошибка: фильма {name} у нас нет :(')
    return res


print(f'Список фильмов: {films}\n')
res = choose_movies(films)
print('Ваш список любимых фильмов:', ', '.join(res))