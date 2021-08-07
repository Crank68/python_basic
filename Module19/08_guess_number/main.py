import random

max_number = int(input('Введите максимальное число: '))
win_number = str(random.randint(1, max_number))
dict_numbers = dict()

while True:
    variants = input('Нужное число есть среди вот этих чисел: ')
    if variants.capitalize() == 'Помогите!':
        if dict_numbers.get('Yes') is None:
            print('Нужна хотя бы одна последовательность чисел с правильным числом. Попытайтесь еще!!!')
        else:
            print(dict_numbers['Yes'].difference(dict_numbers.get('No', set())))
            break
    else:
        variants = set(variants.split())
        if win_number in variants:
            print('Ответ Артёма: Да')
            dict_numbers['Yes'] = variants
        else:
            print('Ответ Артёма: Нет')
            dict_numbers['No'] = variants
