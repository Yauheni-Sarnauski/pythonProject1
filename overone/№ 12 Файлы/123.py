
#################################################3

   # №4
# Создайте словарь из строки ' An apple a day keeps the doctor away'
# следующим образом: в качестве ключей возьмите символы строки,
#а значениями пусть будут числа, соответствующие количеству вхождений данной буквы в строку.
a = 'An apple a day keeps the doctor away'
a = a.replace(' ', '')
#print(a)
s = {}
for i in a:
    d = ([(i, a.count(i))])
    s.update(d)
print(s)
##########################################################################
                                         # вариант 2
a = 'An apple a day keeps the doctor away'
a = a.replace(' ', '')
s = {}
for i in a:
    s[i] = s.setdefault(i,0) + 1
print(s)