# Есть список состоящий из слов и чисел, нужно записать в файл сначала
# слова в порядке их длины, а после слов цифры в порядке возрастания.
a = [1, 22, 29, 31, 41, 8, 'Minsk', 'Rome', 5, 82, 3, 'Sydney', 68, 55, 6, 'Amsterdam', 7, 87, 9, 10]
words = []
numbers = []
for i in a:
    i = str(i)
    if i.isalpha():
        words.append(i)
    elif i.isdigit():
        numbers.append(int(i))

words.sort(key=len)
numbers.sort()


words = ','.join(words)    #  перевод слов из списка в строку


numbers = [str(x) for x in numbers]   # Перевод цифр
                                      # из списка в строку
numbers = ','.join(numbers)           #


mas = words+','+numbers      # сложение слов и цифр


with open('5.txt', 'w') as f:
        f.write(mas)
