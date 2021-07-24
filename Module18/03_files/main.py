file_name = input('Имя файла: ')
forbidden_symbols = '@№$%^&*()'

start_with = [file_name.startswith(symbol) for symbol in forbidden_symbols]

if max(start_with):
    print('Ошибка: название начинается на один из специальных символов')
elif not (file_name.endswith('.txt') or file_name.endswith('.docx')):
    print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx')
else:
    print('Файл назван верно.')
