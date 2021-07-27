import re
while True:
    password = input('Придумайте пароль: ')
    if len(password) < 8:
        print('Пароль не надежный. Меньше 8 символов.')
    elif len(''.join(re.findall(r'\d+', password))) < 3:
        print('Пароль не надежный. Должно быть хотя бы 3 цифр.')
    elif len([result for result in password if result.isupper()]) == 0:
        print('Пароль ненадёжный. Должна быть хотя бы одна заглавная буква.')
    else:
        print('Это надежный пароль!')
