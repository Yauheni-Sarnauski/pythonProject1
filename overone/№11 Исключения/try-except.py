
while True:

    a = input("Введите строку: ")          # Ввод данных через пробел

    arr = a.split()
    try:

        result = int(arr[0])/int(arr[1])
    except ZeroDivisionError:
        print('Деление на ноль недопустимо!')
    except ValueError:
        print('Введена буква требуется цифра')

    else:
        print(result)
        break
    print('Введите числа заново')








