length_list = int(input('Длина списка: '))
numbers_list = [1 if index % 2 == 0 else index % 5 for index in range(length_list)]
print('Результат:', numbers_list)
