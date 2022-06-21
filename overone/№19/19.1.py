#Создайте новую Базу данныхПоля: id, 2 целочисленных поляЦелочисленные поля заполняются рандомно от 0 до 9
# Выберите случайную запись из БД
# Если каждое число данной записи чётное, то удалите эту запись, если нечётное, то обновите данные в ней на (2,2)
# import random
# import sqlite3
# # CОЗДАЕМ базу данных
# conn = sqlite3.connect('Z_1.db')
# cursor = conn.cursor()
# cursor.execute(
#  '''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INTEGER, col_2 INTEGER)''')
# a = random.randint(0, 9)
# b = random.randint(0, 9)
# cursor.execute('''INSERT INTO tab_1(col_1,col_2)
#
#  VALUES (?,?)''', (a, b))
# conn.commit()
# cursor.execute('''SELECT * FROM tab_1''')
# k = cursor.fetchall()
#
# if m[0][0] % 2 == 0 and m[0][1] % 2 == 0:
#     cursor.execute('''DELETE FROM tab_1 WHERE id = ?''', (r))
#     conn.commit()
# else:
#     print('Заходит')
#     cursor.execute('''UPDATE tab_1 SET col_1=2, col_2=2 WHERE id=?''', (r))
#     conn.commit()
# cursor.execute('''SELECT * FROM tab_1''')
# k = cursor.fetchall()
# print(k)



##############################################################################################################

#Создайте метод класса для работы с БД. Достаточно одной колонки в таблице.
# Тип INT.В БД:Если передан 1 аргумент, вставить в таблицу запись с числом
# 3.Если переданы 2 аргумента: проверить или второй аргумент является числом. Если условие верно, то удалить первую запись с БД.
# Если переданы 2 аргумента и их тип значений неизвестен, а 3 аргумент является числом, то обновить значение колонки БД на число 77 в 3 записи.

# import sqlite3
#
# conn = sqlite3.connect('test2.db')
# cursor = conn.cursor()
# cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1 (id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INT ) ''')
# conn.commit()
#
#
# class A:
#     def fun(self, a=None, b=None, c=None):
#         if a is not None and b is None and c is None:
#             print('INSERT 3')
#             cursor.execute('''INSERT INTO tab_1(col_1) VALUES (3)''')
#             conn.commit()
#         elif a is not None and type(b) is int and c is None:
#             print('DELETE')
#             cursor.execute('''DELETE FROM tab_1 WHERE id = 1''')
#             conn.commit()
#         elif a is not None and b is not None and type(c) is int:
#             print('UPDATE')
#             cursor.execute('''UPDATE tab_1 SET col_1=77 WHERE id=3''')
#             conn.commit()
#
# a = A()
# a.fun('c',1,2)
# cursor.execute('''SELECT * FROM tab_1''')
# k = cursor.fetchall()
# print(k)


###########################################################################
#Создать таблицу в Базе Данных с тремя колонками(id, 2 - text, 3 - text). Заполнить её с помощью INSERT данными (3 записи).
# Удалить с помощью DELETE 2 запись. Обновить значения 3-ей записи на: hello world с помощью UPDATE
# *Записать данные с таблицы в файл в три колонки. Первая – id, вторая и третья с данными.


import sqlite3

conn = sqlite3.connect('test3.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1 (id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT, col_2 TEXT ) ''')
d=input()
f=input()
cursor.execute('''INSERT INTO tab_1(col_1,col_2) VALUES (?,?)''', (d, f))
conn.commit()

cursor.execute('''SELECT*FROM tab_1''')
k = cursor.fetchall()
print(k)

cursor.execute('''DELETE FROM tab_1 WHERE id = 2''')
conn.commit()

cursor.execute('''UPDATE tab_1 SET col_1="hello world" WHERE id=3''')
conn.commit()

cursor.execute('''SELECT*FROM tab_1''')
k=cursor.fetchall()
print(k)

f=open('example.txt','w')
cursor.execute('''SELECT*FROM tab_1''')
k = cursor.fetchall()
print(k)
for i in k:
    c = ','.join([str(x) for x in i])
    print(c)
    f.write(c+'/n')
with open('example.txt') as f:
    print(*f)
f.close()

