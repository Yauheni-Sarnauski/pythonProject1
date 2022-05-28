#задание №1
# a = int(input('Введите 7 значное число:'))
# ch=0
# nech=0
# sum=0
# for i in str(a):
#     i=int(i)
#     sum+=i
#     if i%2==0:
#         ch+=1
#     else:
#         nech+=1
# if  ch>nech:
#     print('сумма:',sum)
# else:
#     a=str(a)
#     pr = int(a[0]) * int(a[2]) * int(a[5])
#     print('Произведение 1,3 и 6: ', pr)

  ####################################################

#задание №2

# a=input('Введите текст: ')
# gl='aeoiu'
# g=0
# sogl=0
# for i in a:
#     if i in gl:
#
#         g+=1
#
#     else:
#         sogl+=1
# print('гласные:',g)
# print('согласные:',len(a)-g)

##########################################

#Задача № 3


################################################
# Задача 5
# a = input('Ведите строку')
# b = ''
# c =[]
# for i in a:
#     if i.isdigit():
#         b+=i
#     elif b!='':
#         c.append(b)
#         b = ''
# if b!='':
#     c.append(b)
# print(",".join(c))

#########################

a=input('Введите текст: ')
gl = 0
sogl= 0
lower = ''      # верхний регистр
upper = ''        # нижний регистр
pair_lower = 0  # пара
pair_upper = 0   # пара


for i in a:
    if i in 'AEOIUaeoiu':
        gl += 1
    else:
        sogl += 1
    if i. islower():
        lower += i
        if len(lower)//2 == 1:
            pair_lower += 1
    elif lower != '':
        lower = ''
    if i. isupper():
        upper += i
        if len(upper)//2 == 1:
            pair_upper += 1
    elif upper != '':
        upper = ''

print('гласные:',gl)
print('согласные:',sogl)
print('пары нижнего регистра:',pair_lower)
print('пары верхнего регистра:',pair_upper)
print('длина:',len(a))

