#a = {'pr':['price','quantity']}
magazin = {'apples':[1,50],
           'cherry':[3,20],
           'orange':[2,15],
           'grape':[4,25],
           'tomatoes':[5,10]
           }
for key in magazin:
    print(key,'-',(magazin[key][0]),'-',(magazin[key][1]))

while True:
    a = input('Введите наименование товара:')
    b = int(input('Введите количество товара:'))

    if a in magazin[key] :
        с = print('останок', magazin[key] - b)
        d_1 = dict.fromkeys([a], (magazin[key][0] * b))
