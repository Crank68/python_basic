alphabet = 'abcdefg'

print('1', alphabet[:])
print('2', alphabet[::-1])
print('3', alphabet[::2])
print('4', alphabet[1::2])
print('5', alphabet[:1])

print('6', alphabet[1:][::-1])  # Странно. В задании Все элементы, начиная с конца до предпоследнего.
# А в результате показывают только первый с конца. Я что-то не так понял?

print('7', alphabet[3:4])
print('8', alphabet[:3:-1][::-1])
print('9', alphabet[3:5])
print('10', alphabet[3:5][::-1])
