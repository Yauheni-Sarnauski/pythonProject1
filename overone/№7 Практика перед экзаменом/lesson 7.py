
import random
a=random.randint(1, 10)
b=random.randint(1, 2)
print(a, b)                    # Закоментировать в игровом режиме.
i = 0

if b == 1:
    color = 'red'
    print(color)                  # Закоментировать в игровом режиме.
elif b == 2:
    color = 'black'
    print(color)                   # Закоментировать в игровом режиме.

while i != 5:

    print('Ведите число от 1 до 10:')
    c = input()
    c = int(c)

    print('Ведите цвет \n             color: red or black:  ')
    d = input()
    d = str(d)

    i += 1

    if c == a and d == color:
        break

    else:
        print('Eще ставка')
if c == a and d == color:
    print('Вы угодали!')
if c != a and d != color:
    print('Вы не угодали! \n Правильный ответ:', a, color)

