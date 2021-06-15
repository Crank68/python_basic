def list_append(iterations, text):
    print('\n')
    return [int(input(f'Введите число {text}: ')) for _ in range(iterations)]


first_list = list_append(3, 'первого списка')
second_list = list_append(7, 'второго списка')
first_list.extend(second_list)
first_list = list(set(first_list))

print(first_list)
