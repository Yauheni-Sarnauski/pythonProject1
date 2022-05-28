a = int(input('Введите число a:'))
b = int(input('Введите число b:'))

c=a>b
print(c)
if c:
    print("a больше b")


elif a==3 or b==4 or c==5:
    print('оператор или')

print(not(1==1))

print('слово"Python"обычно подразумевает змею')
print("I'm learning Python")

first_string = 'Слово "Python" обычно подразумевает змею'
second_string = "I'm learning Python"

print('Результат: \n', first_string, '\n', second_string, 12, end='!!!!!!!!!@@@@')
print('Hello')
my_string=''' слово "python"
обычно подразумевает змею I' m learning Python '''
print(my_string)f

a="hello"
b="World"
print(a*2)
c=a+''+b# конкатенация
p = ""  # пустая строка
print(len(a))

a = input("Введите ваше имя")
b = ('Привет,')
print(b+a)
print(3*a)

a='Hello'
b='1234567890'
print(a[0:2],a[:],a[2:])
print(b[0:10:3],b[::-1])
print(a)
b1= int(b[0])
b2=int(b[-1])
print(b1+b2)
print(int(b[0])+int(b[-1]))

import random
a=random.randint(100-999)
print(a)
s=str(a)
a=int(s[0])
b=int(s[1])
c=int(s[2])
print(a+b+c)################


a='Hello'
print(a.upper())
print(a.lower())
print(a.isupper())
print(a.islower())

print('123'.isdigit())
print('ASsdasd'.isalpha())

a = '1_4_aasd_1'
print(a.split('_'))
c = a.split('_')
print('...'.join(c))


a = '1_4_aasd_1'
print(a.index('aasd'))
if '4' in a:
    print('4 есть')
