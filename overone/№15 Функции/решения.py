import random

a = [random.randint(0, 9) for i in range(10)]
print(a)
def sum_chi():
    print(sum(a))

sum_chi()
# вот так сделала
# Кристина Шух17:46
def my_sum():
    s = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    sm = 0
    for i in s:
        sm += i
    print('Сумма чисел списка:', sm)
my_sum()
# Антон Бабков17:46

import random

def sum_a():
    a = [random.randint(1,10) for i in range(5)]
    print(a)
    b = 0
    for i in a:
        b += i
    print(b)
sum_a()
sum_a()
#Юрий Майсеенок17:46
import random

def summa():
    c = [random.randint(0, 5) for _ in range(10)]
    print(c)
    a = 0
    for i in c:
        a += i
    print(a)
summa()
summa()

######################################################################