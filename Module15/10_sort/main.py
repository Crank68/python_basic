import random

random_list = [random.randint(-10, 10) for _ in range(5)]
print(f'Изначальный список: {random_list}')
random_list.sort()
print(f'\nОтсортированный список: {random_list}')

