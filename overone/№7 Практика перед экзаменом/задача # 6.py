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

