import random


def get_indexes(count):
	left = random.randint(1, 9)
	right = random.randint(left, 10)
	return left, right


sticks = list('|' * int(input('Кол-во палок: ')))
quantity_throws = int(input('Кол-во бросков: '))

for throw in range(1, quantity_throws + 1):
	i_start, i_end = get_indexes(len(sticks))
	print(f'Бросок {throw}. Сбиты палки с номера {i_start} по номер {i_end}')
	sticks[i_start - 1:i_end] = list('.' * (i_end - i_start + 1))

print('Результат', ''.join(sticks))

