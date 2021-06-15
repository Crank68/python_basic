shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]


part = input('Название детали: ')

new_list = [1 if i_elem_ == part else i_elem_ for i_elem in shop if i_elem[0] == part for i_elem_ in i_elem]
total_price = sum(new_list[1:len(new_list) + 1:2])
count = new_list.count(1)

print('Кол-во деталий -', count)
print('Общая стоимость -', total_price)
