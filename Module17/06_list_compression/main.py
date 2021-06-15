import random

list_n = [random.randint(0, 1) for _ in range(int(input('Введите кол-во чисел в списке')))]
list_n.sort(reverse=True)
print('Отсортированный список чисел: ', list_n)

while list_n[-1] == 0:
	list_n.pop()

print('Список без нулей', list_n)
