def list_append(iterations, text):
    text_list = text.split('.')
    new_list = [int(input(f'{text_list[0]} {number} {text_list[1]} ')) for number in range(1, iterations + 1)]
    return new_list


skates_count = int(input('Кол-во коньков: '))
skate_sizes = list_append(skates_count, 'Размер.пары: ')
skate_sizes.sort()

people_count = int(input('\nКол-во людей: '))
foot_sizes = list_append(people_count, 'Размер ноги.человека: ')
foot_sizes.sort()

peoples = 0
for foot_size in foot_sizes:
    for skate_size in skate_sizes:
        if foot_size <= skate_size:
            peoples += 1
            skate_sizes.remove(skate_size)
            break

print('\nНаибольшее кол-во людей, которые могут взять ролики:', peoples)
