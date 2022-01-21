# -*- coding: utf-8 -*-
"""112_colab.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1boNh7dYllNqYjOvqGBaWfZaoWrYqZcca

Номер билета, ФИО студента, номер группы

Задача 1. 
Пример описания
"""

# Дан список из чисел и число k, необходимо удалить из !исходного списка все вхождения числа k
print("Введите список чисел через пробел")
a=[int(i) for i in input().split()]
print("Введите число, которое хотите удалить из списка")
k=int(input())
for it in [:]:
    if it==k:
        a.remove(it)
print("Список без выбранного вами числа:")
print(a)

"""Задача 2. Пример описания"""

# #Дано натуральное число A. Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое число n, что f_n = A. Если А не является числом Фибоначчи, выведите число -1.

a = int(input())
if a == 0:
    print(0)
else:
    fib_prev, fib_next = 0, 1
    n = 1
    while fib_next <= a:
        if fib_next == a:
            print(n)
            break
        fib_prev, fib_next = fib_next, fib_prev + fib_next
        n += 1
    else:
        print(-1)

#Дан список, найти в нем второй максимум
print("Введите список чисел через пробел")
l=[int(i) for i in input().split()]
l.sort()
print("Второй максимум списка равен",l[-2])

#Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.

print("Введите список чисел")
b=[int(s) for s in input().split()]
par=0
for i in range(len(b)):
    for j in range(i+1, len(b)):
        if b[i]==b[j]:
            par+=1
print("Количество пар одинаковых чисел равно",par)

#Дан список. Выведите те его элементы, которые встречаются в списке только один раз. Элементы нужно выводить в том порядке, в котором они встречаются в списке

print("Введите список чисел")
d=[int(s) for s in input().split()]
for i in range(len(d)):
    for j in range(len(d)):
        if i!=j and d[i]==d[j]:
            break
    else:
        print("Элементы встречающиеся в данном списке один раз:")
        print(d[i], end=' ')

#Переставьте соседние элементы списка (A[0] c A[1], A[2] c A[3] и т. д.). Если элементов нечетное число, то последний элемент остается на своем месте

print("Введите список чисел")
e=[int(i) for i in input().split()]
for i in range(1, len(e), 2):
    e[i - 1], e[i] = e[i], e[i - 1]
print("Список с переставленными элементами:")
print(' '.join([str(i) for i in e]))

#Дан список из чисел и индекс элемента в списке k. Удалите из списка элемент с индексом k, сдвинув влево все элементы, стоящие правее элемента с индексом k.
#Программа получает на вход список, затем число k. Программа сдвигает все элементы, а после этого удаляет последний элемент списка при помощи метода pop() без параметров. Программа должна осуществлять сдвиг непосредственно в списке, а не делать это при выводе элементов. Также нельзя использовать дополнительный список. Также не следует использовать метод pop(k) с параметром.

print("Введите список чисел")
a = [int(s) for s in input().split()]
print("Введите индекс одного из элементов")
k = int(input())
for i in range(k + 1, len(a)):
    a[i - 1] = a[i]
a.pop()
print("Список без указанного числа:")
print(' '.join([str(i) for i in a]))

#Дан список целых чисел, число k и значение C. Необходимо вставить в список на позицию с индексом k элемент, равный C, сдвинув все элементы, имевшие индекс не менее k, вправо.
#Поскольку при этом количество элементов в списке увеличивается, после считывания списка в его конец нужно будет добавить новый элемент, используя метод append. Вставку необходимо осуществлять уже в считанном списке, не делая этого при выводе и не создавая дополнительного списка.

print("Введите список чисел")
g=[int(s) for s in input().split()]
print("Введите индекс одного из элементов (не последнего) и число, которое хотите добавить в список через пробел")
k, C = [int(s) for s in input().split()]
g.append(0)
for i in range(len(g)-1, k, -1):
    g[i]=g[i - 1]
g[k]=C
print("Список после преобразования:")
print(' '.join([str(i) for i in g]))