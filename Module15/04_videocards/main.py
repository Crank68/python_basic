import random
list_numbers = [2060, 2070, 2080, 3070, 3090]
print('Введите кол-во видеокарт:')
count_graphics_card = int(input())

graphics_card_list = [random.choice(list_numbers) for _ in range(count_graphics_card)]
print('Старый список видеокарт', graphics_card_list)
max_number_card = max(graphics_card_list)

while True:
    try:
        graphics_card_list.remove(max_number_card)
    except ValueError:
        print('Новый список видеокарт:', graphics_card_list)
        break
