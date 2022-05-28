
print('Калькулятор')
a = float(input("Ведите  число:  "))
s = input("математическое действие +,-,/,*    ")
b = float(input("Ведите  число: "))

if s=='+':
    print('Результат: '+ str(a+b))
elif s=='-':
    print('Результат: '+ str(a-b))
elif s=='/':
    print('Результат: '+ str(a/b))
elif s=='*':
    print('Результат: '+ str(a*b))
else:
    print('Ошибка')


