k = int(input('Введите сдвиг: '))
initial_list = input().split()
print('Изначальный список:', initial_list)

if k <= len(initial_list):
    for index in range(len(initial_list)):
        a = (index - k) % len(initial_list)
        print(initial_list[a], end= '')
else:
    print(f'Сдвиг не может быть больше чем кол-во индексов в списке, введите сдвиг меньше {len(initial_list)}')