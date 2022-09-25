while True:
    c = int(input('Введите сумму покупки: '))
    d = int(input('Введи скидку в %: '))
    if c == 0:
        break
    else:
        price = c - (c / 100 * d)
        print(f'Цена за товар: {price}')
        continue