country = {}
country_count = int(input('Кол-во стран: '))

for number in range(1, country_count + 1):
    text = input(str(number) + ' страна: ').split()
    country.update({city: text[0] for city in text[1:]})

for count in range(1, 4):
    city = input(f'{count} город: ')
    result = country.get(city)
    if result is None:
        print(f'По городу {city} данных нет.')
    else:
        print(f'Город {city} распологается в стране {result}')