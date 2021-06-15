def get_new_list(element, copy_list):
    last_element = copy_list[-1]
    while last_element == copy_list[-1]:
        copy_list.pop()
    return copy_list[::-1]


sequence = [int(input('Число: ')) for _ in range(int(input('Кол-во чисел: ')))]
print('Последовательность: ' + ' '.join(str(n) for n in sequence))
sequence = get_new_list(sequence[-1], sequence)
print('нужно прописать чисел', len(sequence))
print('Сами числа: ' + ' '.join(str(n) for n in sequence))
