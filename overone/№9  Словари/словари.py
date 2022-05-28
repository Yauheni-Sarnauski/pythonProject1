                      # создание словарей
d = {}
d = {'dict':2,'dictionary':2}  # ключ и значение
print(d)

############################################

d = dict(short='dict', long='dictionary')
d_2 = dict([(1, 1), (2, 4)])                      #  !!!! можно и цифры и строки

print(d, '\n', d_2)

###############################################

d = dict.fromkeys(['a', 'b'])
d_2 = dict.fromkeys(['a', 'b'], 100)
print(d, '\n', d_2)

#################################################


import random

a = ['a', 2, 'c']

d = {i: random.randint(1, 100) for i in a}
print(d)


d_2 = [3, 9, 8]
print(d_2[0])

print(d, d['a'])

d['v'] = 20           # добавление  элементов !!!!!
print(d)

d['a'] = 100       # замена элементов
print(d)
#
print(len(d))        # длина считается по ключам

#############################################

d = {1: 34, 'a': 23, 5: 32, 6: 'asd'}
del d[5]                               # удаление ключа
print(d)

##################################################


d = {'phone':['pixel','iphone','nokia'],
    'car':['bmw','tesla'],
    'dict_1':{'a': 123, 'b': 'Hello'}
     }
print(d)
print(d['car'][1])
print(d['dict_1']['b'])
print(len(d))

if 'car' in d:
    print('CAR!')



##################################
# Операция not in - определение отсутствия ключа в словаре
# Формирование словаря слов с их числовым эквивалентом

# 1. Сформировать пустой словарь
Words = dict()  # Words = {}

# 2. Ввести количество слов в словаре
count = int(input("Количество слов в словаре: "))

#3. Цикл добавления слов
i = 0
while i < count:
    print("Ввод слов")
    wrd = input("Слово:")
    value = int(input("Значение: "))
    # Если ключа wrd нет в словаре, то добавить пару [wrd:value]
    if wrd not in Words:
        Words[wrd] = value
    i = i + 1
# Вывести сформированный словарь
print(Words)

##############################################


                            # объединение слов и значений

Numbers = dict(zip([1, 2, 3] ,['One','Two','Three']))
print(Numbers)

##################################################
                      # обход словоря
d = {'phone':['pixel','iphone','nokia'],
    'car':['bmw','tesla'],
    'dict_1':{'a': 123, 'b': 'Hello'}
     }
for key in d:                          #1
    print(key)
    print(key, '-', d[key])

#print(d.items())
for key, values in d.items():                #2
    print(key,'--',values)

#######################################

person = {'name': 'Yauheni', 'age':100, 'city':'Minsk'}

print('возраст:',person['age'])

#

##############################
# Значениями словаря могут быть и списки.
# Создайте словарь с ключами BMW, Tesla и списками из 3х моделей в качестве значений.
# Выведите первое и последнее значения каждого из ключей.

d = {'BMW':[1,2,3],'Tesla':[1,2,3]}
print(d['BMW'][0::2])
print(d['Tesla'][0::2])


#Дан словарь с числовыми значениями. Необходимо их все перемножить и вывести на экран.
import random
a = ['a', 'b','c']
d = {i:random.randint(1,10 ) for i in a}
print(d)
r = 1
s = 0
for key, values in d.items():
    print(values)
    r*=values
    s+=values
print(r)
print(s)