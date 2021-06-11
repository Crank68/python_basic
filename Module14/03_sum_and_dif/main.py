def get_count(number):
    return len(str(number))


def get_sum(number):
    result = 0
    for symbol in str(number):
        result += int(symbol)
    return result


number = int(input('Введите число: '))
if number < 0:
    print('Необходимо ввести число больше нуля')
    while True:
        number = int(input('Введите число: '))
        if number > 0:
            break

sum_numbers = get_sum(number)
count_number = get_count(number)
print(f'\nСумма цифр: {sum_numbers}'
      f'\nКол-во цифр в числе: {count_number}'
      f'\nРазность суммы и кол-ва цифр: {sum_numbers - count_number}')