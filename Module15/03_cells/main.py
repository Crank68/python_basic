import random

print('Ввидите кол-во клеток')
cells_count = int(input())
cells_list = [random.randint(-1, 6) for _ in range(cells_count)]
result = ''
for index in range(cells_count):
    value = cells_list[index]
    print(f'Экффективность {index}, клетки: {value}')
    if value < index:
        result += ' ' + str(value)

print('Неподходящие значения:', result)
