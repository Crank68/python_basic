number = int(input('Введите число: '))
if number <= 1:
    print('Необходимо ввести число больше единицы')
    while True:
        number = int(input('Введите число: '))
        if number > 1:
            break

new_list = [symbol for symbol in range(number, 0, -1) if number % symbol == 0 and symbol != 1]
print('Наименьший делитель, отличный от единицы:', min(new_list))
