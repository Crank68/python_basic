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

count_songs = int(input('Сколько песен выбрать: '))
songs_list = [input(f'Название {number} песни: ') for number in range(1, count_songs + 1)]
count_time = 0

for i_elem in violator_songs:
    if i_elem[0] in songs_list:
        count_time += i_elem[1]

print(f'\nОбщее время звучания песен: {round(count_time, 2)} минут')
