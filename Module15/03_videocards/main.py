# TODO здесь писать код
videocard_list = []
new_list = []
newest_list = []
num_video = int(input('Количество видеокарт: '))
count = 1

for _ in range(num_video):
    card = int(input(str(count) + ' Видеокарта: '))
    count += 1
    videocard_list.append(card)

print('Старый список видеокарт:', videocard_list)

newest_list = max(videocard_list)
new_list = [i for i in videocard_list if i != newest_list]
print('Новый список видеокарт:', new_list)

