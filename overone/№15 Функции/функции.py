def a_function():
    print("You jast created a function!")

a_function()

def empty_f():
    pass          # пустая операция

empty_f()

arr = [1,2,3,4]
def fun():                 ########????
   c = 0
   for i in arr:
       c += i
   print("Сумма в списке:", c)
fun()
############################
def add(a,b):
    print(a+b)
    return a+b                     ##?????
add(1,2)
print(add(1,2))

#######################################
def a_function():
    print("You jast created a function!")

print(a_function())

############################

def add(a,b):

    return a+b
print(add(a=2,b=3))   #5

total = add(b=4,a=5)
print(total)              #9

###############################

def keyword_function(a=1,b=2):
    return a+b

print(keyword_function(b=4,a=5))   #9
print(keyword_function())

def mixed_function(a,b=2,c=3):
    return a + b + c

#  mixed_function(b=4,c=5) # ошибка

print(mixed_function(1,b=4,c=5))

print(mixed_function(1))

#######################################

def many(*args,**kwargs):
    print(args)
    print(kwargs)

many(1,2,3,name ="Miki",job="programmer")

######################################################
def function_a():
     global a
     a = 1
     b = 2
     return a+b
def function_b():
    c = 3
    return a + c
print(function_a())
print(function_b())

################################################

def func1(a,b):
    def inner_func(x):
        return x*x*x
    return inner_func(a) + inner_func(b)
print(func1(4,5))

####################################

def sum(a,b): return a + b
print(sum(1,5))

#################################################


def is_year_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
print(is_year_leap(int(input("Введите год"))))
#################################################################

# def season(month):
#     if month in (12,1,2): return "зима"
#     elif month in (3,4,5): return "весна"
#     elif month in (6,7,8):return "лето"
#     elif month in (9, 10, 11):return "осень"
#     else:return "ошибка"
# print(season(int(input("ввести номер месяца"))))
#
