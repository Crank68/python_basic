text = input('Введите текст: ')
hist = dict()

for symbol in text:
    if symbol in hist.keys():
        hist[symbol] += 1
    else:
        hist[symbol] = 1

reversed_hist = {
    value: [key for key, revers_value in hist.items() if value == revers_value] for value in set(hist.values())
                 }

for key, value in reversed_hist.items():
    print(f'{key} : {value}')
