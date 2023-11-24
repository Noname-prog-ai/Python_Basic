violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

# TODO здесь писать код
new_music = []
N = int(input('Сколько песен выбирать?: '))
for i in range(N):
    a = input('Песня: '.format(i + 1))
    new_music.append(a)
count = 0
for k in violator_songs:
    if k[0]  in new_music:
        count += k[1]
print('Общее звучание песен: ',float(round(count, 2)),'минуты')