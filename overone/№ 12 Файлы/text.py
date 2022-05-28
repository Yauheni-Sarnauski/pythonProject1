f = open('1.txt', 'r')
print(f)
print(*f)     # Содержание файла

# #####################################
#
f = open('1.txt', 'r', encoding='utf-8')
print(f)               # для кирилицы
print(*f)
f.close()  # Закрытие файла

#######################################

f = open('1.txt', 'r', encoding='utf-8')
try:
    print(*f) # работа с файлом
finally:
    f.close()

#############################
with open('1.txt', 'r', encoding='utf-8') as f:
    print(*f)


print()              # автоматическое закрытие файла

#######################################3

with open('1.txt', 'r', encoding='utf-8') as f:
    s = f.read()      # количество символов
    # print(f.read())   # оставшиеся символы

print(s, type(s))

#####################################

with open('1.txt', 'r', encoding='utf-8') as f:
    # print(f.readline())
    # print(f.readline())
    s = f.readlines()

print(s)
s_new = []
for i in s:
    i = i.replace('\n','')
    print(i)
    s_new.append(i)
print(s_new)

############################################3

with open('2.txt', 'w') as f:  # создание нового файла
    f.write('Hello Word')      # запись в файл
    f.close()                  # закрытие файла
#######################################

import os

os.rename('2.txt','test.txt') # переименование файла

################################################

import os

print('Текущая дириктория', os.getcwd())   # расположение на компе

os.mkdir('folder')              # создание пустой папки

#############################################

import os
os.chdir('folder')             # изменение текущего каталога
print('Текущая дириктория', os.getcwd())    # вывод текущей папки

########################################

import os
with open('2.txt', 'w') as f:
    f.write("hello \n World")
print('Текущая дириктория', os.getcwd())

####################################################

                    # создание нескольких вложеных папок
import os

os.chdir('folder')       # изменение текущего каталога на 'folder'

os.chdir('..')           # вернутся в текущую дерикторию

os.makedirs('n1/n2/n3')  # сделать несколько вложеных папок

##################################

import os
print('Текущая дириктория', os.getcwd())       # создание файла в папке
os.chdir('folder')
with open('2.txt', 'w') as f:
    f.write("hello \n World")
print('Текущая дириктория', os.getcwd())

###########################################

import os

os.remove("folder/2.txt")             # удаление файла в папке

##############################################

import os
os.rmdir('folder')           # удаление папки

####################################################

import os
os.removedirs('n1/n2/n3')                          # удаление всех указаных папок

#################################################################

# задача
# В файле, в одну строку записаны слова
# и числа через пробел или _ найти сумму всех чисел.

with open('321.txt', 'r') as f:
    # print(*f)
    s = f.read()
s = s.replace('_',' ')
a = s.split()
print(a)
s = 0
for i in a:
    if i.isdigit():
        i = int(i)
        s += i
print(s)

#########################################

# задача №2
# Файл содержит числа и буквы. Каждый записан в отдельной строке.
# Нужно считать содержимое в список так, чтобы сначала шли числа
# по возрастанию, а потом слова по возрастанию их длинны.

with open('12345.txt', 'r') as f:
    # print(*f)
    s = f.readlines()
print(s)
b = []
n = []
for i in s:
    i = i.replace('\n','')
    if i.isalpha():
        b.append(i)
    elif i.isdigit():
        n.append(int(i))
print(b,n)
n.sort()
b.sort(key=len)
mas = n +b
print(mas)