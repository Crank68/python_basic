ip_address = input('IP: ').split('.')
template_isalpha = '{} - не целое число'
template_range = '{} не находится в диапозоне от 0 до 255'
template_good = 'IP - адрес корректен'
template_quantity = 'Адрес - это четыре числа, разделённые точками'

errors = [elem for elem in [
			template_isalpha.format(elem) if not elem.isdigit() else template_range.format(elem)
			if not 0 <= int(elem) <= 255
			else template_quantity if len(ip_address) != 4 else '' for elem in ip_address
] if elem != '']
result = (template_good if len(errors) == 0 else '\n'.join(set(errors)))
print(result)
