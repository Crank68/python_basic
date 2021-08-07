count = int(input('Введите количество пар слов: '))
words = dict()


def dict_add(key, value):
    words[key] = value


def get_value():
    word = input('Введите слово: ').capitalize()
    try:
        print(f'Синоним: {words[word]}')
    except KeyError:
        print('Такого слова в словаре нет.')
        get_value()


for number in range(1, count + 1):
    text = input(f'{number} пара: ').split(' - ')
    dict_add(text[0], text[1])
    dict_add(text[1], text[0])

get_value()
