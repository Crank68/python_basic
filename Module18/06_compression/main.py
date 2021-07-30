text = input('Введите строку: ')
count = 0
current_symbol = text[0]
new_text = []
for symbol in text:
	if current_symbol == symbol:
		count += 1
	else:
		new_text.append(current_symbol+str(count))
		current_symbol = symbol
		count = 1
new_text.append(current_symbol + str(count))
print('\nЗакодированная строка:', ''.join(new_text))
