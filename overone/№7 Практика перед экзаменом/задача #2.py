
#задание №2

a=input('Введите текст: ')
gl='aeoiu'
g=0
sogl=0
for i in a:

    if i in gl:
       b.append(i)
       g+=1

    else:
        sogl+=1
if g== sogl:
    c=','.join(c)
    print('гласные:',g)
print( 'гласные:',gl,'согласные:',sogl)

################################################