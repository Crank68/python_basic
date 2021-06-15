friends = [0 for _ in range(int(input('Кол-во друзей: ')))]
IOUs = int(input('Долговых расписок: '))

for number in range(1, IOUs + 1):
    print(f'\n{number} расписака')
    whom = int(input('Кому: '))
    fromm = int(input('От кого: '))
    money = int(input('Сколько: '))

    friends[whom - 1] -= money
    friends[fromm - 1] += money

print()
for number in range(1, len(friends) + 1):
    print(f'{number}: {friends[number - 1]}')
