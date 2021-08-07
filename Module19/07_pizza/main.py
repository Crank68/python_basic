number_of_order = int(input('Введите кол-во заказов: '))
orders_stat = dict()


def dict_add(any_dict, key, value):
    any_dict[key] = value


for count in range(1, number_of_order + 1):
    order = input(f'{count} заказ: ').split()
    surname = order[0]
    pizza_name = order[1]
    amount = int(order[2])

    if orders_stat.get(surname) is None:
        dict_add(orders_stat, surname, {pizza_name: amount})
    else:
        if orders_stat[surname].get(pizza_name) is None:
            dict_add(orders_stat[surname], pizza_name, amount)
        else:
            orders_stat[surname][pizza_name] += amount
print()
name_keys = sorted(orders_stat.keys())
for sorted_name in name_keys:
    print(sorted_name + ':')
    lower_dict = orders_stat[sorted_name]
    pizza_keys = sorted(lower_dict.keys())
    for sorted_pizza in pizza_keys:
        print(f'   {sorted_pizza}: {lower_dict[sorted_pizza]}')

