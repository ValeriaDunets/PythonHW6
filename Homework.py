#Заполните массив элементами арифметической прогрессии. 
#Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
#Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
#Каждое число вводится с новой строки.
"""""
a1 = int(input("Введите первый элемент: "))
d = int(input("Введите разность: "))
n = int(input("Введите кол-во эдементов: "))

for i in range(n):
    print(a1 + i * d, end=' ')

"""


#Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума). 
# Список можно задавать рандомно
#На входе : [ 1, 5, 88, 100, 2, -4]
#33
#200
#Ответ: [2, 3]

from random import randint as rd

list1 = [rd(0,100) for _ in range(10)]
print(list1)

min_val = int(input("Введите миним значение: "))
max_val = int(input("Введите максим значение: "))

for i in range(len(list1)):
    if min_val <= list1[i] <= max_val:
        print(i, end=' ')