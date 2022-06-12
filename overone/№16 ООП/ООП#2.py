# class Car:
#                      # создание методов класса
#     def start(self):
#         print('Двигатель заведен')
#
# car_a = Car
# print(car_a)

##############################
# создание класса Car
# class Car:
#                      # создание методов класса
#     def __srt__(self):
#         return "Car class object"
#
#         def start(self):
#             print('Двигатель заведен')
#
# car_a = Car()
# print(car_a)

##########################

# class Phone:
#
#     def __init(self,color, model):
#         self.color = color           #?????????????
#         self.model = model
#
#     def check_sim(self, mobile_operator):
#         if self.model == 'I785' and mobile_operator == 'MTS':
#             print('Your mobile operator is MTS')
#
# my_phone = Phone('red','I785')
# my_phone.check_sim('MTS')
#
#     @staticmethod
#     def nodel_hash(model):
#         if nodel == 'I785':
#             return 34565
#         elif model == 'K498':
#             return  45567
#         else:
#             return None
#
# print(Phone.model_hash('I785'))
# my_phone = Phone('red','I785')
# print(my_phone.model_hash('K498'))
#
#
# @classmethod
# def toy_phone(cls, color):
#     toy_phone = cls(color,'ToyPhone')
#     return toy_phone
# Phone.toy_phone('Red')
# print(Phone.toy_phone('Red').model)


###################################################
# # Класс Human
# # Создайте класс Human.
# # Определите для него два статических поля: default_name и default_age.
# # Создайте метод init(), который помимо self принимает еще два параметра: name и age. Для этих параметров задайте значения по умолчанию, используя свойства default_name и default_age. В методе init() определите четыре свойства: Публичные - name и age. Приватные - money и house.
# # Реализуйте справочный метод info(), который будет выводить поля name, age, house и money.
# # Реализуйте справочный статический метод default_info(), который будет выводить статические поля default_name и default_age.
# # Реализуйте метод earn_money(), увеличивающий значение свойства money.
# class Human:
#     default_name = 'A'
#     default_age = 'B'
#     def __init__(self,name = default_name ,age = default_age):
#         self.neme = name
#         self.age = age
#         self.__hause = None
#         self.__money = 0
#     def info(self):
#         print(self.name, self.__money,self.__house, self.age)
#
#     @staticmethod
#     def default_info():
#         print(Human.default_name, Human.default_age)
#     def earn_money(self,plus):
#         self.__money += plus
#         print(self.__money)
#
# human = Human('Mark',25       ####################??????????/
# human.info()
# human.earn_money(100)
# human.info()

###################################################

# class Phone:
#
#     def __init__(self):
#         self.is_on = False
#
#     def turn_on(self):
#         pass
#
#     def call(self):
#         pass
# class MobilePhone(Phone):
#         def __init__(self):
#             super().__init__()
#             self.battery = 0
#
#         def charge(self,num):
#             pass
#             print(f'Charging battery up to ... {self.battery}%')
#
# my_mobile_phone = MobilePhone()
# print(dir(my_mobile_phone))

#############################################

# class Venicle:
#     def vehicle_method(self):
#         print("Это родительский метод из класса vehicle")
#
# class Car(Venicle):
#     def car_nethod(self):
#         print("Это метод из класса Car")
#
# class Cycle(Venicle):
#     def cycleMethod(self):
#         print("Это дочерний метод из класса Cycle ")
#
# car_a = Car()
# car_a.venicle_method()
# car_b = Cycle()
# car_b.venicle_method()



# class Camera:
#     def camera_method(self):
#         print("Это родительский метод из класса Camera")
# class Radio:
#     def radio_method(self):
#         print("Это родительский метод из класса Radio")
# class CellPhone(Camera, Radio):
#     def cell_phone_method(self):
#         print("Это дочерний метод из класса CellPhone")
# cell_phone_a = CellPhone()
# cell_phone_a.camera_method()
# cell_phone_a.radio_method()

#####################################
#Класс House
# 1. Создайте класс House
# 2. Создайте метод init() и определите внутри него два динамических свойства:
# _area и _price. 3. Свои начальные значения они получают из параметров метода init()
# 4. Создайте метод final_price(), который принимает в качестве параметра размер
# скидки и возвращает цену с учетом данной скидки.
#
# Класс SmallHouse
# 1. Создайте класс SmallHouse, унаследовав его функционал от класса House
# 2. Внутри класса SmallHouse переопределите метод init() так, чтобы он
# создавал объект с площадью 40м2
#
# Класс Human
#  1. Реализуйте приватный метод make_deal(), который будет отвечать за техническую
# реализацию покупки дома: уменьшать количество денег на счету и присваивать ссылку
# на только что купленный дом.
# В качестве аргументов данный метод принимает объект дома и его цену.
# 2.  Реализуйте метод buy_house(), который будет проверять, что у человека достаточно денег
# для покупки, и совершать сделку. Если денег слишком мало - нужно вывести предупреждение в
# консоль. Параметры метода: ссылка на дом и размер скидки