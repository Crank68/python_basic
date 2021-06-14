films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия', 'Город грехов', 'Мементо', 'Отступники', 'Деревня']
# TODO Строка кода не должна превышать 120 символов (РЕР 8)
favorite_films = []

for _ in range(5):
    name_film = input('Введите имя любимого фильма: ')
    if name_film in films:
        favorite_films.append(name_film)
print('Список фильмов добавленных в избранное:\n' + '\n'.join(favorite_films))
