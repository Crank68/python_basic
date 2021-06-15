shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

count = 0
total_price = 0
part = input('Название детали: ')

for i_elem in shop:
    if i_elem[0] == part:
        count += 1
        total_price += i_elem[1]

print('Кол-во деталий -', count)
print('Общая стоимость -', total_price)
