elements = [1,3,'a',6,'b']
print(elements)

elements= list()
print(elements)

import random
c=[random.randint(0,9) for i in range(10)]

print(c)
print(c[0],c[-1])
print(c[2:])

c.append(7777)
c.append('Hi!')
print(c)


l=[12,43,213,645,'as',23]
l.insert(0,'hello')
l.insert(3,5544)
print(l)
l[3]='world'
print(l)


l=[12,43,213,645,'as',23]  ############ как со срезами
del l[2:4]
print(l)

l.remove('as')  #  если повторяется удоляет только один первый элемент
print(l)

###########################################################

l=[12,43,213,645,'as',23]
print(12 in l)               # выведется  True
if 12 in l:
    print('yes')

################################################################
a=[1,2,3,'as']
b=[5,6,7]
print(a+b)
               # или
c=a+b
print(c)

d=['f','s','h']
d.extend(c)    #добовляем список  d
print(d)

##########################################################

a=[1,2,3,'as']
b=a  # cсылка на список
b.append(77)
a.append(55)
print(id(a),id(b))
print(a,b)           # так неправильно

c=a.copy()
c.append('fhn')
print(id(a),id(c)) #!!!!!!!!!!!!!!!!!!!!!!!!
#print(id(a),id(b))

##########################################################

a=[1,2,3,'as']
for i in a:                 #for
    print(i)
#
print('_'*10)
b = [1, 2, 3, 'as']       #whileprint(c)
b_l = len(b)
i = 0
while i < b_l:
    print(b[i])
    i+=1

######################################################################

a=[1,2,3,4,5]
a.clear()
print(a)
b=[1,1,1,1,2,3,4]
print(b.count(1),'index элемента 4:',b.index(4))
x=b.pop(4)                            #удаление индекса
print(b)                              #и возвращение его

print(x)
b.reverse()                            # переворот словаря
print(b)

##################################################################

b=[1,1,1,1,21,9,7,3,4,3,4]
b.sort()
print(b)
b.sort(reverse=True)                 # обратный реверс
print(b)

s = ['afgf','ahgjljij','aljjgghf','fg','ghj']
s.sort(key=len)               # сортировка по длине, если() то по алфавиту
print(s)

##########################################

a = [1,5,6,9,'fg',[5,5,6,8]]
print(a[5][2])

##############################################

b=[2,3,5,7,6,44,5,'ghfg','fsgd']

b.reverse()               # обратный реверс
print(b)

b=[2,3,5,7,6,44,5,'ghfg','fsgd']


a = [27, 1, 43, 2, 3, 8]
print(a[::-1])



s=[2,54,54,64,6,20,50,5,85]  # заменить элемент списка
a=s.index(20)

s[a]=200
print(s)

