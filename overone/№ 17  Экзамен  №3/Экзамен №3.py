
                                    #  задание №1
  #1. Напишите функцию, которая будет принимать номер кредитной карты и показывать
# только последние 4 цифры. Остальные цифры должны заменяться звездочками



def card_4(card):
    return '*' * len(card[:-4]) + card[-4:]

number = input("Введите номер кредитной карты: ")
print(card_hide(number))

                                   #  задание №2

#2. Напишите функцию, которая проверяет: является ли слово палиндромом

def Palindrome(s):
    # Используем встроенную функцию
    rev = ''.join(reversed(s))

    # Проверяем строки на равенство
    if (s == rev):
        return True
    return False

s = "SAIPPUAKIVIKAUPPIAS"
ans = Palindrome(s)
print(ans)

###############################################################################

def palindrom(a):
    if a == a[::-1]:
        print("yes")
    else:
        print("no")


str_ = input("Введите слово для проверки: ")
palindrom(str_)




##############################################################


                                    # Класс Tomato:
# 1. Создайте класс Tomato
# 2. Создайте статическое свойство states, которое будет содержать все стадии созревания помидора
# 3. Создайте метод __init__(), внутри которого будут определены два динамических protected свойства: 1) _index - передается параметром и
# 2) _state - принимает первое значение из словаря states
# 4. Создайте метод grow(), который будет переводить томат на следующую стадию созревания
# 5. Создайте метод is_ripe(), который будет проверять, что томат созрел (достиг последней стадии созревания)
#
#

# Класс TomatoBush
# 1. Создайте класс TomatoBush
# 2. Определите метод __init__(), который будет принимать в качестве параметра количество томатов и на его основе будет создавать список объектов класса Tomato.
# Данный список будет храниться внутри динамического свойства tomatoes.
# 3. Создайте метод grow_all(), который будет переводить все объекты из списка томатов на следующий этап созревания
# 4. Создайте метод all_are_ripe(), который будет возвращать True, если все томаты из списка стали спелыми
# 5. Создайте метод give_away_all(), который будет чистить список томатов после сбора урожая



#
# Класс Gardener
# 1. Создайте класс Gardener
# 2. Создайте метод __init__(), внутри которого будут определены два динамических свойства: 1) name - передается параметром, является публичным и
                                    # 2) _plant - принимает объект класса Tomato, является protected
# 3. Создайте метод work(), который заставляет садовника работать, что позволяет растению становиться более зрелым
# 4. Создайте метод harvest(), который проверяет, все ли плоды созрели. Если все - садовник собирает урожай. Если нет - метод печатает предупреждение.
# 5. Создайте статический метод knowledge_base(), который выведет в консоль справку по садоводству.
#
# Тесты:
# 1. Вызовите справку по садоводству
# 2. Создайте объекты классов TomatoBush и Gardener
# 3. Используя объект класса Gardener, поухаживайте за кустом с помидорами
# 4. Попробуйте собрать урожай
# 5. Если томаты еще не дозрели, продолжайте ухаживать за ними
# 6. Соберите урожай
#

class Tomato:
    # Статическое свойство, cтадии созревания помидора
    states = {0: 'зародыш', 1: 'рост', 2: 'цветение', 3: 'зеленый_помидор', 4: 'красный_помидор'}

    def __init__(self, index):
        self._index = index
        self._state = 0

    # Перевод на следующую стадии созревания
    def grow(self):
        if self._state < 4:
            self._state += 1
        print(f'Tomato {self._index} перешло в следующую стадию: {Tomato.states[self._state]}')

    # Проверка что томат созрел
    def is_ripe(self):
        if self._state == 4:
            print('Помидоры созрели. Урожай собран!!!')
        else:
            print('Еще рано!!! Помидоры еще зеленные')

class TomatoBush:
    def __init__(self, amt):
        self.tomatoes = [Tomato(index) for index in range(1, amt)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        for tomato in self.tomatoes:
            tomato.is_ripe()

    def give_away_all(self):
        self.tomatoes = []

class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        print(self.name,'работает....')
        self._plant.grow_all()
        print(self.name,'закончил работу')

    def harvest(self):
        print(self.name, 'проверяет все ли плоды созрели')
        print('Проверка завершена')
        if self._plant.all_are_ripe():
            return self._plant.give_away_all()


    @staticmethod
    def knowledge_base():
        print('''Плод томата в среднем растет 42 дня. 
Время сбора урожая наступает в конце вегетационного периода, 
когда помидоры находятся на зрелой стадии, обычно в конце лета.''')

Gardener.knowledge_base()
plant_t_bush = TomatoBush(2)
gardener = Gardener('Adrian', plant_t_bush)
gardener.work()
gardener.work()
gardener.work()
gardener.harvest()
gardener.work()
gardener.harvest()


################################################

# 3. Решите задачу
#
# Класс Tomato:
# 1. Создайте класс Tomato
import random
class Tomato:
# 2. Создайте статическое свойство states, которое будет содержать все стадии
# созревания помидора
    states={1:'vysazhen rostok',2:'est plod', 3:'plod vyros', 4:'plod sozrel'}
# 3. Создайте метод __init__(), внутри которого будут определены два динамических
# protected свойства: 1) _index - передается параметром и 2) _state - принимает первое
# значение из словаря states
    def __init__(self, index):
        self._index = index
        self._state = 0
# 4. Создайте метод grow(), который будет переводить томат на следующую стадию
# созревания
    def grow(self):
        self._next_stage()
        print('rastet, zreet')
    def _next_stage(self):
        if self._state < 4:
            self._state += 1
        print(f'Tomato {self._index+1} -- {Tomato.states[self._state]}')
# 5. Создайте метод is_ripe(), который будет проверять, что томат созрел (достиг
# последней стадии созревания)
    def is_ripe(self):
        if self._state==4:
            return True
        else:
            return False
# Класс TomatoBush
# 1. Создайте класс TomatoBush
# 2. Определите метод __init__(), который будет принимать в качестве параметра
# количество томатов и на его основе будет создавать список объектов класса
# Tomato. Данный список будет храниться внутри динамического свойства tomatoes.
class TomatoBush:
    def __init__(self, qtomatoes): #Число томатов на кусте
        self.tomatoes=[Tomato(i) for i in range(0, qtomatoes)]
# 3. Создайте метод grow_all(), который будет переводить все объекты из списка
# томатов на следующий этап созревания
    def grow_all(self):
        for i in self.tomatoes:
            i.grow()
# 4. Создайте метод all_are_ripe(), который будет возвращать True, если все томаты из
# списка стали спелыми
    def all_are_ripe(self):
        print('Proverka zrelosti')
        return all([i.is_ripe() for i in self.tomatoes])
# 5. Создайте метод give_away_all(), который будет чистить список томатов после
# сбора урожая
    def give_away_all(self):
        self.tomatoes.clear()
        # print('Net tomatov')
# Класс Gardener
# 1. Создайте класс Gardener
# 2. Создайте метод __init__(), внутри которого будут определены два динамических
# свойства: 1) name - передается параметром, является публичным и 2) _plant -
# принимает объект класса Tomato, является protected
class Gardener:
    def __init__(self, name, plant):
        print('Sadim rostok')
        self.name = name
        self._plant = plant
# 3. Создайте метод work(), который заставляет садовника работать, что позволяет
# растению становиться более зрелым
    def work(self):
        print('Polivaem, udobraem')
        self._plant.grow_all()
        print('Polili, udobrili')
# 4. Создайте метод harvest(), который проверяет, все ли плоды созрели. Если все -
# садовник собирает урожай. Если нет - метод печатает предупреждение.
    def harvest(self):
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print('Tomaty sozreli i sobrany')
        else:
            print('Tomaty esche ne sozreli')
# 5. Создайте статический метод knowledge_base(), который выведет в консоль справку
# по садоводству.
    @staticmethod
    def knowledge_base():
        print('Spravka po sadovodstvu: Kolhoz imeni Michurina')
# Тесты:
# 1. Вызовите справку по садоводству
# 2. Создайте объекты классов TomatoBush и Gardener

tomatobush=TomatoBush(random.randint(1,8)) # число томатов на кусте, случайно
# tomatobush=TomatoBush(2) # число томатов на кусте
gardener=Gardener('Michurin', tomatobush)
gardener.knowledge_base()
# 3. Используя объект класса Gardener, поухаживайте за кустом с помидорами
# 4. Попробуйте собрать урожай
# 5. Если томаты еще не дозрели, продолжайте ухаживать за ними
# 6. Соберите урожай
gardener.harvest()
gardener.work()
gardener.harvest()
gardener.work()
gardener.harvest()
gardener.work()
gardener.harvest()
gardener.work()
gardener.harvest()
