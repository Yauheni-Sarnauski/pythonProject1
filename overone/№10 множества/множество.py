num_set = {1,6,4,2,10,50,100,70,40}
print(num_set)

num_set = {1,6,4,2,'A','B','C'}
print(num_set)

b = {'a','b','c'}
print(b)

c = {1,2,3,5,4,2,5,1}
print(c)
print(len(c))

########################################

a = [1,42,5,"g",6,7,'v',2,2,2]
print(len(a))
c = set(a)
print(c,len(c))

v = list(c)
print(v)

######################################

a = {1,42,5,"g",6,7,'v',2,2,2}

for i in a:
    print(i)

print(1 in a)     # проверка наличия



################################

a = {123, 546, 8, 35, 5}
a.discard(0)                  #  удаление если нет то без ошибки
print(a)

a.remove(8)   #удаление выдаст ошибку при удалении несуществующего множества
print(a)



x=a.pop()   # удаление и возвращение элемента
print(a, x)



months_a = {1,23,5,2,3,4,5,7}
manths_b = {2,15,6,7,2,5,1,9}
all_months = months_a.union(manths_b)
print(all_months)                      # или
print(manths_b|months_a)

x = {1,2,3}
y = {4,3,6}
z = {7,4,9}
output = x.union(y,z)  # объединение списков
print(output)                       #или
print(x|y|z)

############################
x = {1,2,3}
y = {4,3,6}
print(x&y)       #  пересечения

A = {1, 2, 3}     # разница между множествами
B = {4, 3, 6}
print(A-B)   # 1, 2
print(B-A)   # 4, 6

###################################

string_set = {'Nicholas', "michelle",'John','Mercy'}
x = string_set.copy()
print(x)


a_a = {1,2,3,4,5}              # проверяет наличие пересечения
b_b = {7,8,9,10,6}          # если есть то false , нет True
x = a_a.isdisjoint(b_b)
print(x)

my_set = frozenset([1 ,2, 3, -10,40])   # неизменяемое множество
print(type(my_set))

a = {123, 546, 8, 35, 5}      # добавление в множество
a.add('gsdgh')
a. add(235)
print(a)

##############################################





a = [1,6,5,45,2,5]
x = set(a)
if len(a)!=len(x):
     print('Есть дубликаты')
else:
    print('Нету дубликатов')



a ={1,6,5,45,2,5}
x = frozenset([6 ,9, 2, -50,11])

print(a|x)
print(a&x)


