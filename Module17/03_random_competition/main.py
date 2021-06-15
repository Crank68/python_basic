import random

members_1 = [round(random.uniform(5, 10), 2) for _ in range(20)]
members_2 = [round(random.uniform(5, 10), 2) for _ in range(20)]
winners = [members_1[index] if members_1[index] > members_2[index] else members_2[index] for index in range(20)]

print('Первая команда:', members_1)
print('Вторая команда:', members_2)
print('Победители тура:', winners)
