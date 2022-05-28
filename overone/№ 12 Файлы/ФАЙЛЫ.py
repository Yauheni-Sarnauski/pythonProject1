with open('222.txt', 'w') as f:
    while True:
     a = input()  # запись в файл
     if a == '':
        break
     f.write(a + '\n')
     continue
