
#Задача №4

import random
a = int(input('Количество чисел:' ))
b = [random.randint(1,100)for i in range(a)]
print(b)
c =  int(input('Выбрать интересуемую цифру:'))
d=0
for i in b:
    for e in str(i):
        if int(e)==d:
            d+=1
print('Цифра',c,'встречается', d,раз)



Задача 5
a = input('Ведите строку')
b = ''
c =[]
for i in a:
    if i.isdigit():
        b+=i
    elif b!='':
        c.append(b)
        b = ''
if b!='':
    c.append(b)
print(','.join(c))

    d = input("Сделайте ставку, число и цвет: ")
    if b==1 :
        print ('черный')
    elif b==2:
        print('черный')
    else:
         print(b)

    elif int(d) == c:
        print("Победа")
    else:
         print("Попробуйте еще")
print(b)
    if b==1:
        color1 = 'красный'
    if  b==2:
        color2 = 'черный'
