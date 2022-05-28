i=0
while i<10:
    print(i)
    i=i+1         # i+=1

#################
i=0
while i<10:
    print(i)
    if i==7:
        break
    i=i+1        # i+=1

i=0
while i<10:
    i = i + 1                 ###???????????      ОТЛИЧИЕ ОТ ВСЕХ ОСТАЛЬНЫХ
    if i==7
        continue            ##### возврат в начало цикла
    print(i)


#Необходимо вычислить сумму чисел от 1 до 50 и результат вывести на экран.
i=1
# r=0
while i<=50:
    r +=  i
    i=i+1
    print(i,r)
print(r,end=' ')

r_1=0
for i in range(1,51):
    r_1+=i
print(r_1,end=' ')

i=1
r=0
while i<=10:
    i+=1
    print(i**2)

i=0
b=1
while i<=125:
        i+=2######################
        b*=i
print(b)   ###################


################################
for i in range(3):
    print(i)
    if i ==1:
        break
else:
    print('Готово')

i=0
while i<3:
    if i==1:
        break
    print(i)
    i+=1
else:
    print("готово")

i=15
b=0
while i<=15:
    i-=1
    print(i)

i=15
while 0<i:
    print(i)
    i =i-1
# #
i=7
a=[]
while i<98:
    print(i)
    i +=7
    a.append(i)
print(a,len(a) )

i=0
while i<10:
    i+=1
i-=10
print(i)