import random

container_count = int(input('Введите кол-во контейнеров: '))

containers = [random.randint(0, 200) for _ in range(container_count)]
containers.sort(reverse=True)

print('Вес контейнера: ', end='')
print('\nВес контейнера: '.join(str(container) for container in containers))

new_container = int(input('\nВведите вес нового контейнера: '))
count = 1

for value in containers:
    if value < new_container:
        break
    count += 1

print('Номер, куда встанет новый контейнер:', count)
