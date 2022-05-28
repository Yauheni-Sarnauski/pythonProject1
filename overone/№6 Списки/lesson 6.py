a = [4, 6, 'pу' ,'tell' ,78]
b = [44,'hello',56,'exept' ,3]
c=a+b
print(c)                           #Объединить два списка.

c[3]=6
print(c)                           #Добавьте элемент 6 на 3 индекс в объединённом списке.

del c[2:7:4]
del c[-2]
print(c)                           #Удалите все текстовые переменные в объединённом списке

print(len(c))                      #  Посчитайте количество элементов списка в объединённом списке




a = [4, 6, 'py', 'tell', 78]
b = [44, 'hello', 56, 'exept', 3]
a.extend(b)
a.insert(3,6)
print(a)
for i in a:
    if str(i).isalpha():  #if type(i) is str:
        a.remove(i)
             #a.sort()
print(a)
l = len(a)
