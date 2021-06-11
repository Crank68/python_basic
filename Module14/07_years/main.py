year1 = int(input('Введите первый год: '))
year2 = int(input('Введите второй год: '))
ideal_list = []

for year in range(year1, year2 + 1):
    str_year = str(year)
    if len(set(str_year)) == 2 and str_year.count(str_year[0]) != 2:
        ideal_list.append(str_year)

print(f'Годы от {year1} до {year2} с тремя одинаковыми цифрами:\n'+'\n'.join(ideal_list))
