import random
a = int(input('Количество чисел:' ))
b = random.randint(1,100)

for i in range(a):
print(b)
c =  int(input('Выбрать интересуемую цифру:'))
d=0
for i in b:
    for e in str(i):
        if int(e)==d:
            d+=1
print('Цифра',c,'встречается', d,раз)


a=[11,51,6,16,5]
a=