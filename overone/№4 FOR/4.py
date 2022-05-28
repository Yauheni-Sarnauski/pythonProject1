for i in range(6):
    print(i)
    print('привет!')

for i in range(10,0,-2):
    print(i,end=' ')

a=10
b=0
c=-2
for i in range(a,b,c):
    print(i,end=' ')

a='я учу Python'
for i in a:
    print(i)
    if i =='P':
        print('Python')
print('Результат')

# вывести числа от 1 до 15 в порядке убывания.
for i in range(15,0,-1):
    print(i, end=' ')

a='я учу PYTHON python'
b=''
for i in a:

    if i.isupper():
        print(b, end=' ')
        b=b+i
print('Результат',b)








a = input('Введите строку: ')
b = input('Введите символ: ')
c = ''
for i in a:
    # print(i)
    if i != b:
        print(c)
        c = c + i
print(c)


a = int(input("Введите начало"))
b = int(input("Введите конец"))
c=int(input("Введите шаг"))
for i in range(a,b,c):
    print(i, end=' ')





a=[1,45,7,8,9,0]# массив чисел
a_s=['hello','world','abc']# массив строк
print(a,len(a))
print(a_s,len(a_s))



for i in a:
    print(i)

    if i==7:
        break # выход из цикла на указанном элементе

for i in a:
    if i == 7:
        continue # пропуск указанного элемента массива
    print(i)
print('готово')


a=[1,2,2,3,4,5,6,7,8,9,10]
b=[]
for i in a:
    if i %2==0:
        b. append(i)
print(b)
b.append(777777)    #добавление символа
print(b)
print('ЦИФРА 2 ПОВТОРЯЕТСЯ:',a.count(2))



a=[1,2,2,3,4,5,6,7,8,9,10]
c=0
for i in a:
     print(c, end=' ')
     c=c+i
print('результат',c)

a=[1,2,2,3,4,5,6,7,8,9,10]
b=[]
for i in a:
    if i %2==0:
        b. append(i)
print(b)


for i in range(5):
    if i % 2 == 0:
     continue
    print(i)
