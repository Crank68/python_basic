words = input('Строка: ').split()
len_words = [len(elem) for elem in words]
result = words[len_words.index(max(len_words))]
print('Самое длиное слово: ', result)
