#Создайте новую Базу данных.
# Поля: id, 2 целочисленных поля.
# Целочисленные поля заполняются рандомно от 0 до 9.
# Посчитайте среднее арифметическое всех элементов без учёта id.
# Если среднее арифметическое больше количества записей в БД, то удалите четвёртую запись БД.

import random
import sqlite3
# CОЗДАЕМ базу данных
conn = sqlite3.connect('name1.db')
cursor = conn.cursor()

a = random.randint(0,9)
b = random.randint(0,9)
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INT,col_2 INT)''')
cursor.execute('''INSERT INTO  tab_1(col_1,col_2) VALUES(?,?)''', (a,b))
conn.commit()

cursor.execute('''SELECT*FROM tab_1''')
k = cursor.fetchall()
print(k)

##############################################################################3

#
# import sqlite3
# import random
#
# # Создаем новую базу данных
# conn = sqlite3.connect('namedb4.db')
# # Создаем объект курсор который позволяет взаимодействовать с БД и добавлять записи
# cursor = conn.cursor()
# # Создадим таблицу с id и 2 целочисленными полями
# cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INT, col_2 INT)''')
# # Заполняем таблицу данными
# d = random.randint(0, 100)
# f = random.randint(0, 100)
# data = cursor.execute('''INSERT INTO tab_1(col_1, col_2) VALUES (?,?)''', (d, f))
# # Сохраняем изменения
# conn.commit()
# # Выбираем только значения из столбцов
# cursor.execute('''SELECT col_1, col_2 FROM tab_1''')
# k = cursor.fetchall()
# print(k)
# s = len(k) * 2
# print('Количество элементов в таблице: ', s)
#
# result = []
# for i in k:
#     a = 0
#     for j in i:
#         a += j
#     result.append(a)
# # print(result)
# b = sum(result)
# print('Сумма всех элементов таблицы: ', b)
# # Среднее арифметическое всех элементов
# r = b / s
# print('Среднее арифметическое: ', r)
#
# if r > len(k):
#     cursor.execute('''DELETE FROM tab_1 WHERE id=4''')
#     conn.commit()
#     cursor.execute('''SELECT*FROM tab_1''')
#     q = cursor.fetchall()
#     print(q)
#
#
# ########################################################################
#
#
# import sqlite3
# import random
# # Создаём Базу данных
# conn = sqlite3.connect('name_bd1.db')
# # Создаем объект cursor, который позволяет нам взаимодействовать с базой данных и добавлять записи
# cursor = conn.cursor()
#
# # Целочисленные поля заполняются рандомно от 0 до 9.
# d = random.randint(0,9)
# f = random.randint(0,9)
#
#
# cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INT,col_2 INT) ''')
# cursor.execute('''INSERT INTO tab_1(col_1,col_2) VALUES (?,?)''', (d, f))
# conn.commit()
#
# cursor.execute('''SELECT*FROM tab_1''')
# k = cursor.fetchall()
# print(k)
# # Посчитайте среднее арифметическое всех элементов без учёта id.
# sch=0
# sch1=0
# for i in k:
#     sch1+=(int(i[1])+int(i[2]))
#     print(sch1)
#     sch+=1
#     print(sch)
#
# sr_arifm=sch1/(sch*2)
# print(sr_arifm,'>',sch)
# if sr_arifm>sch:
# # Если среднее арифметич больше записей в БД,
# # то Удаление записи из таблицы по id 4-го номера
#     cursor.execute('''DELETE FROM tab_1 WHERE id = 4''')
#     conn.commit()
#
# cursor.execute('''SELECT*FROM tab_1''')
# k=cursor.fetchall()
# print(k)


###############################################################

import sqlite3
import random
conn=sqlite3.connect('m_name.db')
cursor=conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INT, col_2 INT)''')
a=random.randint(0,9)
print('a',a)
b=random.randint(0,9)
print('b',b)
cursor.execute('''INSERT INTO tab_1(col_1, col_2) VALUES (?,?)''', (a,b))
conn.commit()
cursor.execute('''SELECT*FROM tab_1''')
k=cursor.fetchall()
print('БД: ',k)
x=[]
y=[]
q=[]
w=0
for i in k:
    y=''.join(([str(y) for y in i]))
    q=[y[1],y[2]]
    x+=q
    w += int(y[1]) + int(y[2])
# print('Данные без id ', x)
print('Кол-во записей в БД: ',len(k))
print('БД текущая запись: ',y)
# print('Сумма эл-тов без учета id: ',w)
# print('Кол-во эл-тов без учета id: ',len(x))
print('Среднее арифметическое: ', float(w/len(x)))
if float(w/len(x))>len(k):
    cursor.execute('''DELETE FROM tab_1 WHERE id=4''')
    cursor.execute('''SELECT*FROM tab_1''')
    k=cursor.fetchall()
print('Отработанная БД: ',k)

