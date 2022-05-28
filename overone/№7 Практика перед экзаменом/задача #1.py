задание №1
a = int(input('Введите 7 значное число:'))
ch=0
nech=0
sum=0
for i in str(a):
    i=int(i)
    sum+=i
    if i%2==0:
        ch+=1
    else:
        nech+=1
if  ch>nech:
    print('сумма:',sum)
else:
    a=str(a)
    pr = int(a[0]) * int(a[2]) * int(a[5])
    print('Произведение 1,3 и 6: ', pr)
