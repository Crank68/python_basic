vowel_list = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
text = input('Введите текст: ')

vowel_in_text = [elem for elem in text if elem in vowel_list]
print('Список гласных букв:', vowel_in_text)
print('Длина списка', len(vowel_in_text))
