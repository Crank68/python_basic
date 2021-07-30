violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}
song_amount = int(input('Сколько песен выбрать? '))
song_total_time = sum([violator_songs.get(input(f'Название {number + 1} песни: '), 0) for number in range(song_amount)])
print('Общее время звучания песен:', round(song_total_time, 2), 'минут')
