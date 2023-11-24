# TODO здесь писать код
n = []
k = []
count_skates = int(input('Введите кол-во роликов: '))
counter = 0

for i in range(1, count_skates + 1):
    print('Размер', i, 'пары: ', end = '')
    n.append(int(input('')))
count_people = int(input('\nКоличесво людей: '))
for i in range(1, count_people + 1):
    print('Размер ноги', i, 'человека: ', end = '')
    k.append(int(input('')))
for num in k:
    for j in range(len(n)):
        if n[j] >= num:
            n.remove(n[j])
            counter += 1
            break
print('\nНаибольшее количество людей, которые могут взять ролики:', counter)