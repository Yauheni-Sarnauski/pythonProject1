w='нет'
dict1={'Банан': [6,50]}
dict3={'Яблоко': [4,30]}
dict4={'Мандарин': [5, 40]}
dict5={'Киви': [7, 20]}
dict2={}
for i in dict1:
    print(i, '-', dict1[i])
for i in dict3:
    print(i, '-', dict3[i])
for i in dict4:
    print(i, '-', dict4[i])
for i in dict5:
    print(i, '-', dict5[i])
while True:
    b = input('Введите наименование товара:')
    c = int(input('Введите количество товара:'))

    if b in dict1 :
        aa = print('сталось на складе',dict1[b][1] - c)
        d_1 = dict.fromkeys([b],(dict1[b][0] * c))
        for key in dict1:
            dict2[key] ='к оплате',dict1[b][0] * c, 'осталось',dict1[b][1] - c
        print(dict2)

    if b in dict3 :
        aa = print('сталось на складе',dict3[b][1] - c)
        d_3 = dict.fromkeys([b],(dict3[b][0] * c))
        for key in dict3:
            dict2[key] ='к оплате',dict3[b][0] * c, 'осталось',dict3[b][1] - c
        print(dict2)

    if b in dict4 :
        aa = print('сталось на складе',dict4[b][1] - c)
        d_4 = dict.fromkeys([b],(dict4[b][0] * c))
        for key in dict4:
            dict2[key] ='к оплате',dict4[b][0] * c, 'осталось',dict4[b][1] - c
        print(dict2)
    if b in dict5:
        aa = print('сталось на складе',dict5[b][1] - c)
        d_5 = dict.fromkeys([b],(dict5[b][0] * c))
    for key in dict5:
            dict2[key] ='к оплате',dict5[b][0] * c, 'осталось',dict5[b][1] - c
       #     print(dict2)

    ww = str(input('хотите что то ещё купить:'))
    if w == ww:
    # print(dict2)
    # break
#
# d = dict.fromkeys(['a', 'b'])
# d_2 = dict.fromkeys(['a', 'b'], 100)
# print(d, '\n', d_2)
#

    shop = {'bread': [1.5, 40], 'milk': [2, 30], 'eggs': [3, 20]}  # цена за штуку!
    print('Каталог товаров магазина: ')
    for key in shop:
            print('Наименование товара: ', key, '-', 'По цене, руб./шт: ', shop[key][0], '-', 'Количество шт.: ',
                  shop[key][1])
    print('При покупке от 10 шт. скидка 50%!')
    p = input('Здравствуйте! Вам пакет нужен? ')
    p = p.lower()  # все опустила до нижнего регистра
    pack = 0.2  # цена пакетика
    basket = 0  # счетчик для корзины
    s = 1  # счетчик для суммы одного прохода цикла, и каждый раз сумму добавляем в корзину
    while True:
            a = input('Введите название выбранного товара (продукта): ')
        a = a.lower()  # все опустила до нижнего регистра
        if a == 'exit':  # выход из цикла, покинули магазин
                break
        if a not in shop:  # исключили неправильность ввода
                print('Введенного товара нет в магазине! Проверьте правильность ввода, спасибо, ')
            continue
        b = int(input('Введите требуемое количество товара (продукта): '))
        if b > shop[a][1]:  # на случай если сразу ввели количество больше имеющегося
                print('Требуемое количество недостпуно! Доступно', shop[a][1], 'шт.')
            continue
        shop[a][1] -= b  # отнимает от каталога купленное количество товара
        if shop[a][1] < 0:  # если по мере покупок закончился товар
                print('Требуемое количество недостпуно! Доступно', shop[a][1], 'шт.')
        s = shop[a][0] * b  # сумма одного прохода цикла
        if b >= 10:  # типа скидка, целых 50%, чтоб удобно считать
                s *= 0.5
        basket += s
    if p == 'yes':  # не забыли посчитать пакетик
            basket += pack
    d = input('У Вас есть дисконтная карта нашего магазина? ')
    d = d.lower()  # все опустила до нижнего регистра
    basket1 = 1  # корзина для учета дисконта
    if d == 'yes':
            basket1 = basket * 0.99  # корзина с учетом дисконта
        print('Сумма покупки составляет: ', basket1, 'бел. руб.', '\n', 'Спасибо за покупку. Ждем Вас снова!')
    else:
        print('Сумма покупки составляет: ', basket, 'бел. руб.', '\n', 'Спасибо за покупку. Ждем Вас снова!')
    print('Товары доступны к слудующей покупке: ')
    for key in shop:
            print('Наименование товара: ', key, '-', 'По цене, руб./шт: ', shop[key][0], '-', 'Количество шт.: ',
                  shop[key][1])

