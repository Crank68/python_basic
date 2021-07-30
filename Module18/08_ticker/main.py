text_1, text_2 = input('Первая строка: '), input('Вторая строка: ')

shift = text_2.index(text_1[0])
if text_2 == ''.join([text_1[index - shift] for index in range(len(text_1))]):
    print('Первая строка получается из второй со сдвигом.', shift)
else:
    print('Первую строку нельзя получить из второй с помощью циклического сдвига.')
