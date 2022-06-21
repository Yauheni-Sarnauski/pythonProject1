import sqlite3
# CОЗДАЕМ базу данных
conn = sqlite3.connect('name.db')
# создаем обьект cursor, который позволяет нам взаимодействовать с базой даных и добавлять записи
cursor = conn.cursor()
# создаем таблицу с двумя текстовыми колонками
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT,col_2 TEXT)''')
# ЗАПОЛНЯЕМ ТАБЛИЦУ ДАННЫМИ
cursor.execute('''INSERT INTO  tab_1(col_1,col_2) VALUES('hello','world')''')
#
conn.commit()

d = "red"
f = "black"
# Заполняем таблицу при помощи переменных
cursor.execute('''INSERT INTO  tab_1(col_1,col_2) VALUES(?,?)''',(d,f))
conn.commit()

cursor.execute('''SELECT*FROM tab_1''')
k = cursor.fetchall()
print(k)

############################################
# получение первого результата
a = 'hello'
cursor.execute('''SELECT * FROM tab_1 WHERE col_1 = 'hello' ''')

# # список записей отсортированных относительно третьей колонки
# cursor.execute('''SELECT * FROM tab_1 ORDER BY col_3 ''')

#  #  все записи начинающиеся на 7 в третьей колонке
# cursor.execute('''SELECT * FROM tab_1 WHERE col_3 like '7% ''')


###############################################
             # задание 1
#Создайте новую Базу данных.
# В ней создайте таблицу с тремя полями, два текстовых, одно – целое число.
# Число запрашивается с клавиатуры, а слова задаются статически.
# * Выведите каждую запись в отдельную строку


conn = sqlite3.connect('m_name.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT, col_2 TEXT, col_3 INT)''')
n = int(input('Введите число:  '))
cursor.execute('''INSERT INTO tab_1(col_1,col_2, col_3) VALUES ('name', 'data', ?)''',  (n,))
conn.commit()
cursor.execute('''SELECT*FROM tab_1''')
k = cursor.fetchall()
print((k))
for i in k:
    x=','.join([str(x) for x in i])
    print(x)




##################################################################
# удаление
cursor.execute('''DELETE FROM tab_1 WHERE id = 1''')
conn.commit()
cursor.execute('''DELETE FROM tab_1 WHERE col_1 ='red' ''')
conn.commit()
cursor.execute('''SELECT*FROM tab_1''')
k = cursor.fetchall()
print(k)

# обновление базы данных
t = 3
cursor.execute(('''UPDATE tab_1 SET col_1='world' WHERE id = ?''',(t,)))
conn.commit()
cursor.execute('''SELECT*FROM tab_1''')
k = cursor.fetchall()
print((k))