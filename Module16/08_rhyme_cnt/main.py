peoples = list(range(1, int(input('Кол-во человек: ')) + 1))
drop_out = int(input('Какое число в считалке? '))
print(f'Значит, выбывает каждый {drop_out} человек')
print('\nТекущий круг людей:', peoples)
print(f'Начало счёта с номера {peoples[0]}')
count = 1

while len(peoples) != 1:
    for i_elem in peoples:
        if count == drop_out:
            index = peoples.index(i_elem)
            peoples.remove(i_elem)
            count = 1 - index
            print(f'Выбывает человек под номером {i_elem}')
            if len(peoples) == 1:
                break
            print('\nТекущий круг людей:', peoples)
            if i_elem > peoples[-1]:
                print(f'Начало счёта с номера {peoples[0]}')
            else:
                print(f'Начало счёта с номера {peoples[index]}')
            break
        count += 1

print('\nОстался человек под номером', peoples[0])
