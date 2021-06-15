guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while True:
    amount = len(guests)
    print(f'\nСейчас на вечеринке {amount} человек: {guests}')
    choice = input('Гость пришёл или ушёл? ')

    if choice == 'Пора спать':
        print('\nВечеринка закончилась, все легли спать.')
        break

    name_quest = input('Имя гостя: ')
    if choice == 'пришёл':
        if amount == 6:
            print(f'Прости, {name_quest}, но мест нет')
        else:
            guests.append(name_quest)
            print(f'Привет, {name_quest}!')
    elif choice == 'ушёл':
        try:
            guests.remove(name_quest)
            print(f'Пока, {name_quest}!')
        except ValueError:
            print('Гостя с таким именем не на вечеринке нет.')
    else:
        print('Такого действия нет.')
