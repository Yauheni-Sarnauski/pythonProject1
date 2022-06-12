#Калькулятор.
#Создайте класс, где реализованы функции(методы) математических операций. А также функция, для ввод данных.

class Calculator:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b
    def sub(self):
        return self.a - self.b
    def mul(self):
        return self.a * self.b
    def raising(self):
        return self.a ** self.b

    def div(self):
        return self.a / self.b
    def divi1(self):
        return self.a // self.b
    def div2(self):
        return self.a % self.b

    def exit(self):
        print('Вычисления завершены')

    a = float(input('a: '))
    b = float(input('b: '))
    obj = Calculator()

while True:


        с = input("+ - / *  0 // %: ")
        if с == "+":
            print('Результат:', obj.add(self.a, self.b))
        elif с == "-":
            print('Результат:', obj.sub(self.a, self.b))
        elif с == "*":
            print('Результат:', obj.mul(self.a, self.b))
        elif с == '**':
            print('Результат:', obj.raising(self.a, self.b))
        elif с == "/":
            print('Результат:', obj.div(self.a, self.b))
        elif с == "//":
            print('Результат:', obj.div1(self.a, self.b))
        elif с == '%':
            print('Результат:', obj.div2(self.a, self.b))




