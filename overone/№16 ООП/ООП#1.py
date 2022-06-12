class Car:
    pass

car_object = Car()  #

print(dir(Car))

class Car:
    color = 'Grey'

    def turn_on(self):
        pass
    def ride (self):
        pass
car_object = Car()
print(dir(Car))


class Car:
    #статические
    default_color = 'Gray'
    default_weight = 3000
    ################ Динамичечские поля
    def __init__(self,color,model):
        self.color = color
        self.model = model
    def turn_on(self):
        return 'Я метод!'
    def info(self):
        print(self.color, self.model)

car_obj = Car('Red', 'ABC')
car_obj_2 = Car('Geen','BCA')
car_obj.info()
car_obj_2.info()

print(car_obj.default_color)
print(car_obj_2.default_color)
print(car_obj.default_color)
print(car_obj_2.color)








#####################################################
class Car:
    # Статические поля (переменные класса)
    default_color = 'Grey'

    # Динамические поля (переменные объекта)
    def init(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    # Методы
    def first(self):
        print('Автомобиль заведен')

    def second(self):
        print('Автомобиль заглушен')

    def third(self):
        print(self.year)

    def fourth(self):
        print(self.type)

    def fifth(self):
        print(self.color)


car_obj = Car('Red', 'BMW', 2021)
print(car_obj.default_color)
print(car_obj.color)
print(car_obj.type)
print(car_obj.year)
print(car_obj.first())
print(car_obj.second())
print(car_obj.third())
print(car_obj.fourth())
print(car_obj.fifth())


############################################

class TheExample:
    a = 2
    b = 3

    def __init__(self, t, r):
        self.t = t
        self.r = r

    def func(self):
        c = 5
        print(c)

    def func1(self):
        return self.a + self.b

    def func2(self):
        return self.t ** self.r


example = TheExample(4, 2)

print(TheExample.a)
print(example.func1())
print(example.func2())
example.func()