def get_count(number):
    return len(str(number))


def change_number(number):
    new_number = str(number).split('.')
    return float(new_number[0][::-1] + '.' + new_number[1][::-1])


number1 = float(input('Введите первое число: '))
number2 = float(input('Введите второе число: '))

new_number1 = change_number(number1)
new_number2 = change_number(number2)

print('\nПервое число наоборот:', new_number1)
print('Второе число наоборот:', new_number2)
print('Сумма:', new_number1 + new_number2)