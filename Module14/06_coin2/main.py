import math


def get_result(x, y, r):
    if math.sqrt(x ** 2 + y ** 2) <= r:
        return '\nМонетка где-то рядом'
    else:
        return '\nМонетки в области нет'


print('Введите координаты мотеки:\n')
x = float(input('X: '))
y = float(input('Y: '))
radius = float(input('Введите радиус: '))

print(get_result(x, y, radius))
