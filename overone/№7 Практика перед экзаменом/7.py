
print("100 200 300 400".count("0"))
print("100 200 300 400".count("0",3,7))
print("100 200 300 400".count("0",3))

#############################################

s='aaadddoki'  # посчитать гласные и согласные
g=0
sogl=0
gl='aeoiu'
for i in s:
    if i in gl:
        g+=1
        print(i)
    else:
        sogl+=1
print('гласные:',g)
print('согласные:',sogl)# или
print('согласные:',len(s)-g)


##########################################################################

a = int(input("Ведите  число 1:  "))
b = int(input("Ведите  число 2:  "))
c = int(input("Ведите  число 3:  "))
s = [a, b, c]
s.sort()
print('среднее число:'s[1])

a = int(input('Введите число a: '))
b = int(input('Введите число b: '))
c = int(input('Введите число c: '))

if a > b and a < c:
    print('Среднее число:', a)
elif b > a and b < c:
    print('Среднее число:', b)
else:
    print('Среднее число:', c)

d = [a, b, c]
d.sort()
print('Среднее число:', d[1])






###########################################

Список из 7 цифр. Если четных цифр в нем больше чем нечетных, то найти сумму всех его цифр, если нечетных больше, то найти произведение 1 3 и 6 элемента.
s=[1,2,3,4,5,6,7]
ch=0
nech=0
for i in s:
    if i %2==0:
        ch+=1

    else:
        nech+=1

print('Чётные: ', ch, 'Нечётные: ', nech)
if ch>nech:
    sm=sum(s)                    #сумма всех s
    print('сумма:',sm)
elif  nech>ch:
    pr = s[0] * s[2] * s[5]
    print('Произведение: ', pr)

a='235689'

print(a[::-1])

s=int(input('число:'  ))
print(s[::-1])

for i in a:
    s += i
print(s)
for i in a:
    p *= i
print(p)

pr = 1
for i in c:
    pr *= i
print('Произведение цифр: ', pr)


##########################################################

s = input('Введите строку: ')
n_s = s.replace(' ', '')
print(n_s)
if n_s == n_s[::-1]:
    print('Cрока палиндром')
else:
    print('Не палиндром')


print(
    "$100 $200 $300 ".count("$"),
    "$100 $200 $300 ".count("$",5,10),
    "$100 $200 $300 ".count("$",5)
)

