
print('Калькулятор')
def sum (a,b): return a + b
def subtraction(a,b): return a - b
def multiplication(a,b): return a * b
def division(a,b): return a / b
def exponentiation(a,b): return a ** b

a = float(input('a: '))
b = float(input('b: '))

while True:
    c = input('+ - / *  0 // %: ')
    if c == '+':                               #Сложение
        print(sum(a,b))
    elif c == '-':                               #Вычитание
        print(subtraction(a,b))
    elif c == '*':                               #умножение
        print(multiplication(a,b))
    elif c == '/'or '//'or '%':                               # возведение в степень
        print(division(a,b))
    elif c == '**':                               # возведение в степень
        print(exponentiation(a,b))
    elif c == '0':                               #Завершение вычислений
        break
print('Вычисления завершены')
try:
    c = a / b
except ZeroDivisionError:
    print("Деление на ноль не допустимо!")

# else:
#     print(c ** 2)
finally:
    print('Вычисления завершены')
print('Вычисления завершены')