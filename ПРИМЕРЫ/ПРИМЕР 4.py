a=['fdgx','hrddzf','hgfgcfbx']
b=len(a)
print(a,b)

#######################
a=[1,3,5,8,7,6]
for i in a:
    print(i)

##########################
a=[1,3,5,8,9,7,6]
for i in a:
    print(i)
    if i ==9:
        break

#####################
for i in range(4):
    print(i)

range(4, 8)
range(4, 8, 1)
range(1, 9, 3)
range(10, 5, -2)

#######################
for i in "Я учу Python":
    print(i)

#####################
for i in range(15, 0, -1):
    print(i)

#############################3
arr = ['string1', 'string2', 'string3']
l = len(arr)
print(arr,'Длинна: ', l)

########################

arr = [1, 7, 9, 10]

for i in arr:
    print(i)

############################
arr = [1, 7, 9, 10]

for i in arr:
    print(i)
    if i == 9:
        break


for i in arr:
    if i == 9:
        continue
    print(i)

##########################
a = [10, 2, 3]
print(a)
a.append(7)
print(a)

#####################

Практическое 1

a = input('Введите строку: ')
b = input('Введите символ: ')
c = ''
for i in a:
    if i != b:
        c += i
        print(c)
print('Результат: ', c)

#################################

Практическое 2
a = int(input('Введите начало: '))
b = int(input('Введите конец : '))
c = int(input('Введите шаг : '))
for i in range(a, b, c):
    print(i)

###############################################################

for i in range(4):
    print(i)
    print('Привет!')

for i in range(1, 10, 2):
    print(i)
a = 10
b = 0
c = -2
for i in range(a, b, c):
    print(i, end=' ')
a = 'Я учу Python'
for i in a:
    print(i)
    if i == 'P':
        print('Python')

print('Результат')
# Необходимо вывести числа от 1 до 15 в порядке убывания.
for i in range(15, 0, -1):
    print(i, end=' ')
a = 'я учу PYTHON python'
b = ''
for i in a:
    # print(i)
    if i.isupper():
        print(b)
        b = b + i

print('Результат', b)

a = input('Введите строку: ')
b = input('Введите символ: ')
c = ''
for i in a:
    # print(i)
    if i != b:
        print(c)
        c = c + i
print(c)

a = [1, 45, 7, 8, 9, 0]  # массив чисел
a_s = ['hello', 'world', 'abc']  # массив строк
print(a, len(a))
print(a_s, len(a_s))


for i in a:
    print(i)
    if i == 7:
        break
print('Готово')

for i in a:
    if i == 7:
        continue
    print(a)
print('Готово')

a = [1, 2, 2, 2, 4, 6, 8, 9]
b = []
for i in a:
    if i % 2 == 0:
        b.append(i)
print(b)
b.append(777777)
print(b)
print('Цифра 2 повторяется: ', a.count(2))

a = [1, 2, 3]
c = 0
for i in a:
    print(c)
    c = c + i
print('Результат: ', c)





