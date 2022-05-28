a = 100/0
print(a)



try:
    k = 1/0                      # обработка исключений
except ZeroDivisionError:
    k = 0
print(k)

try:
    k = 1/0                      # обработка исключений
except ArithmeticError:
    k = 0
print(k)

try:
    int('asd')
   # 1/0
except Exception as e:
    print(' Произошла ошибка', e)


my_dict = {'a':1,'b':2,'c':3}
try:
    value = my_dict['d']
except KeyError:
    print("Ключа не существует!")


my_list = [1,2,3,4,5]
try:
    my_list[6]
except IndexError:
    print('Этого индекса нет в списке!')


my_dict = {'a':1,'b':2,'c':3}
try:
    value = my_dict['d']
except KeyError:
    print("Ключа не существует!")
except IndexError:
    print('Этого индекса нет в списке!')
except :
    print('Произошла другая ошибка!')


my_dict = {'a':1,'b':2,'c':3}
try:
    value = my_dict['d']
except (KeyError,IndexError):
    print('Произошла ошибка KeyError  или IndexError!')



my_dict = {'a':1,'b':2,'c':3}
try:
    value = my_dict['d']
except KeyError:
    print("Произошла ошибкаKeyError!")
finally:
    print('Оператор  finally выполнен!')

my_dict = {'a':1,'b':2,'c':3}
try:
    value = my_dict['a']
except KeyError:
    print("Произошла ошибкаKeyError!")
else:
    print('ошибок не произошло!')


my_dict = {'a':1,'b':2,'c':3}
try:
    value = my_dict['a']
except KeyError:
    print("Произошла ошибкаKeyError!")
else:
    print('ошибок не произошло!')
finally:
    print('Оператор  finally выполнен!')



a = int(input("Введите число:"  ))
b = int(input("Введите число:"  ))
try:
    c = a/b
except ZeroDivisionError:
    print("Деление на ноль не допустимо!")

else:
    print(c**2)
finally:
    print('Оператор  finally выполнен!')
