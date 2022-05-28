a = int(input("Введите целое число  "))
b = int(input("Введите целое число  "))
c = float(input("Ведите дробное число  "))
s = input("введите строку  ")

print(s)
print(a+b+c)

a=int(input('Введите число:'))
if a > 0:
   print('a БОЛЬШЕ 0')
   print(12)

if True:
  print('hello')

print(2==2)



a = int(input('Введите число:'))
if a > 0:
    print('a БОЛЬШЕ 0')
else:
    print('a меньше 0')


a = int(input('Введите число:'))
if a > 1:
    print('a БОЛЬШЕ 0')
elif a==0:
    print('a равно 0')
elif a == -7:
    print('a равно -7')
else:
    print('a меньше 0')

#проверка числа четное или не четное
a = int(input('Введите число:'))
print(a%2)
if a%2==0:
    print('четное число')
else:
    print('число нечетное')

#and(и) or(или) not(не)

a = int(input('Введите число a:'))
b = int(input('Введите число b:'))
c = int(input('Введите число c:'))
if  a==1 and b==3 and c==2:
    print('a=1 b=3 c=2')
elif a==3 or b==4 or c==5:
    print('оператор или')

print(not(1==1))

a = int(input('порядковый номер пальца руки :'))

if  a==1:
    print('Мизинец')
elif  a==2:
    print('Безымяный')
elif a == 3:
     print('Средний')
elif a == 4:
    print('Укозательный')
elif  a==5:
    print('Большой')
else:
    print('Нету такого')



