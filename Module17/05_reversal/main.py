text = input('Введите текст: ')

text_list = text.split('h')
print(text_list[0] + 'h' + text_list[1][::-1] + 'h' + text_list[2])
