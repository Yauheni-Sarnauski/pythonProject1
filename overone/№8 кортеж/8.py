#Кортежи

a = (1,2,3,4,5,6)
b = (1,)
print(a,b)

##########################################
a = (1,2,3,4,5,6)
b = [1,2,3,4,5,6]
print(a.__sizeof__())                 # обьем в байтах
print(b.__sizeof__())

#######################################
a = (1,2,3,4,5,6)                        #срезы
print(a[0:3])
print(a[:3])
print(a[1:])
print(a[2::2])

#################################
a = (1,3,4,'abc',54)                  # изменение корте
print(a)
#a[0]=12
b = tuple(a)
c = list(a)
print(c)
print(b)

################################################
a = (1,3,4,'abc',54)
a = list(a)                   # изменение кортежа через его изменение
print(a)
a.append(75)
print(a)
a = tuple(a)
print(a)

####################################################

a = (1,3,4, [1,4,2,'a'],54)          # список в картеже
a[3].append(777)
print(a)
print(a[2]+10)

#####################################
a = (1,3,4,'abc',54)    #   длина кортежа
print(len(a))

#######################
a = (1,3,4,'abc',54)       # объединение кортежей
b = (3,564,45)
z = a + b
print(z)

v =  a*2                  # умножение
print(v)

print(v.count(1))          # методы

################################################
a = (34,6,7,9,100)
print(max(a))          # сортировка по числом
print(min(a))
print(sum(a))                # сумма чисел

##################################################
a = ('asd','sd','asddas')
print(max(a,key=len))      # сортировка по длине строки
print(min(a,key=len))

for i in a:
    print(i, len(i))
ind_max = a.index(max(a, key=len))
print(a[ind_max], len(a[ind_max]))



###################################################################3
import random
c=[random.random() for i in range(10)]
print(c)
a=tuple(c)
print(max(a))
print(min(a))

##################################################################3


a = tuple(2, 3, 5, 1, 3, 4, 1, 3, 0, 5)
b = tuple(-2, 0, -1, -4, -4, -2, -1, 0, -3, 0)
d = a + b
print(d, d.count(0))

c = [random.randint(0,10) for i in range(10)]
d = [random.randint(-5,0) for i in range(10)]
c = tuple(c) + tuple(d)
print(c, c.count(0))


a = ('one', 'two', 'three')
a = ('1','gcf','jgfry','1',1,6,8)
c = ','.join(a)
c = ','.join([str(i) for i in a])
print(c)


a = ('1','gcf','jgfry','1',1,6,8)

c = ','.join(a)
#c = ','.join([str(i for i in a)])
print(c)


a = ('sd', 'weriq', 'ggg', 1, 88)
print(', '.join([str(i) for i in a]))




###########################################







A = (13, 5, 43, 49, 67, 32, 12, 98, 6, 10, 34, 20, 55, 68, 14, 60, 14)
B = (53, 21, 4, 23, 76, 3, 43, 12, 54, 342, 21)

if sum(A) > sum(B):
    print('cумма больше в кортеже А ')
else:
    print('cумма больше в кортеже B ')

print('min A', min(A), 'Номер - ', A.index(min(A)) + 1)
print('min B', min(B), 'Номер - ', B.index(min(B)) + 1)


Str_value = "String"
for index in range ( len ( Str_value )):
    print ( Str_value[index])

a = "String"
for i in range(len(a)):
    print(a[i])


















