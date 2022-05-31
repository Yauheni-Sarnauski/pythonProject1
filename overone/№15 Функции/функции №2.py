# def factorial(n):
#     if n!=0:
#         return n * factorial(n-1)   #факториал
#     else:
#         return 1
# print((factorial(5)))

################################################

# def func(x):return x
#
# a1 =func
# a2 = a1
# print(a2(10))

##############################################

# product = lambda x,y:x*y
# print(product(2,3))
#
# power = lambda x=1,y=2:x**y
# square = power
# print(square(5))

#########################

# def nul(a):
#     def helper(b):
#         return a * b
#     return helper
# print(nul(3)(2))

########################################
#
# def nul(a):
#     def helper(b):
#         return a * b
#     return helper
# three_nul = nul(3)
# print(three_nul(5))

###################################

# def first_test():
#     print("test function 1")
#
# def second_test():
#     print("test function 2")
#
# def simpl_decore(fn):
#     def wrapper():
#         print("start function")
#         fn()
#         print("stop function")
#     return wrapper
#
# first_test_wrapped = simpl_decore(first_test)
# second_tst_wrapped = simpl_decore(second_test)
#
# first_test_wrapped()
# second_tst_wrapped()

#########################################

# def simpl_decore(fn):
#     def wrapper():
#         print("start function")
#         fn()                                        # более удобный способ
#         print("stop function")
#     return wrapper
#
# @simpl_decore
# def first_test():
#     print("test functoon 1")
#
# first_test()

#########################################################33

# def parm_transfer(fn):
#     def wrapper(arg):
#         print(" Start function:"+ str(fn.__name__)+ "().with param:"+ str(arg))
#         fn(arg)
#     return  wrapper
#
# @parm_transfer
# def print_sqrt(num):
#     print(num ** 0.5)
#
# print_sqrt(4)

#################################################

#задание №1
#написать функцию которая определяет количество
# разрядов введенного целого числа
# def discharge(n):
#     i = 0
#     while n > 0:
#         n = n//10
#         i += 1
#     return i
#
# num = abs(int(input('Введите число: ')))
# print('Количество разрядов:', discharge(num))
#
#
# a=input('Введите число: ')
# def razr(a):
#     print(len(a))
# razr(a)
#
# def number_mat():
#     ch = 0
#     for i in str(a):
#         ch += 1
#     print('Количество разрядов введенного числа: ', ch)
#########################################

# Задание №2
#Создайте функцию, которая принимает на вход неограниченное количество позиционных и именованных аргументов,
# в качестве результата функция должна возвращать только позиционные аргументы с нечетными индексами и ключевые,
# значения которых являются строками

# def f(a,b,c,*args):
#     n = list(filter(lambda x: isinstance(x,str),[a,b,c]))
#     res = [a,b,c]+ list(args)
#     l = [ ]
#     for c, i in enumerate(res):
#         if c % 2 and not i in [a,b,c]:l +=[i]
#     return (n + l)
#
# print(f('git',1,5,6,8,9,"bios"))
# print(f(1,9,56,87,'num',6))
#

# def many(*args,**kwargs):
#     print(args)
#     for i in args:
#         if args.index(i)%2!=0:
#             print(args.index(i),'-',i)
#             a.append(i)
#     for value in kwargs.values():
#         if type
#
#
#
# many(1,2,3,name ="Miki",job="programmer")





#####################################################