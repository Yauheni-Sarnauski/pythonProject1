# Задача 5
a = input('Ведите строку')
b = ''
c =[]
for i in a:
    if i.isdigit():
        b+=i
    elif b!='':
        c.append(b)
        b = ''
if b!='':
    c.append(b)
print(','.join(c))


