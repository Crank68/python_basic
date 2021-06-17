russian_alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
text = input('Введите сообщение: ').lower()
shift = int(input('Сдвиг: '))
i_max = len(russian_alphabet) - 1
len_alp = len(russian_alphabet)
forbidden_symbols = '!., '  # Это список нужно расширить.

a = 5
b = 6

a,b = b,a

new_text = [russian_alphabet[russian_alphabet.index(symbol) + shift
            if russian_alphabet.index(symbol) + shift <= i_max
            else shift - (len_alp - russian_alphabet.index(symbol))]
            if symbol not in forbidden_symbols else symbol for symbol in text]

print(''.join(new_text))
