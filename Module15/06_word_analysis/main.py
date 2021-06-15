word = input('Введите слово: ')
count = 0
for symbol in word:
    if word.count(symbol) == 1:
        count += 1

print('Кол-во уникальных символов:', count)
