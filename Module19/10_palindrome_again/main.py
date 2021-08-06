text = input('Введите строку: ')
set_text = set(text)
list_symbols_count = [0 for symbol in set_text if text.count(symbol) % 2 != 0]
if 0 <= len(list_symbols_count) <= 1:
    print('Можно сделать палиндромом')
else:
    print('Нельзя сделать палиндромом')
