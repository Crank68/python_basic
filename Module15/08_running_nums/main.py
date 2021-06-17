import random

numbers_list = [random.randint(-10, 10) for _ in range(5)]

shift = int(input('Сдвиг: '))
print('Изначальный список:', numbers_list)
new_number_list = [numbers_list[number] for number in range(-shift, 5 - shift)]
print('Сдвинутый список:', new_number_list)
