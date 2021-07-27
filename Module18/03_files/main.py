file_name = input('Имя файла: ')
forbidden_symbols = '@№$%^&*()'

if file_name[0] in forbidden_symbols:
    print('Ошибка: название начинается на один из специальных символов')
elif not (file_name.endswith('.txt') or file_name.endswith('.docx')):
    print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx')
else:
    print('Файл назван верно.')
