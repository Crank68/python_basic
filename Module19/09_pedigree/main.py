family = dict()
people_count = int(input('Введите количество человек: '))

for pair_number in range(1, people_count):
	couple = input(f'{pair_number} пара: ').split()
	if family.get(couple[1]) is None:
		family[couple[1]] = 0
		family[couple[0]] = 1
	else:
		family[couple[0]] = family[couple[1]] + 1

print('\n“Высота” каждого члена семьи:')
for key in sorted(family.keys()):
	print(key, family[key])
