punctuation_marks = ',.:!-?"'
massage = input('Сообщение: ').split()
reverse_message = []
for word in massage:
    if word.isalpha():
        reverse_message.append(word[::-1])
    else:

        new_word = ''
        temp_world = ''
        for symbol in word:
            if symbol.isalpha():
                new_word = symbol + new_word
            else:
                temp_world += new_word + symbol
                new_word = ''

        reverse_message.append(temp_world + new_word)

print('Новое сообщение:', ' '.join(reverse_message))
