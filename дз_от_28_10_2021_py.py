
#Написать функцию, которая вычисляет среднее арифметическое элементов массива, переданного ей в качестве аргумента.

import numpy
print("Введите элементы массива через пробел")
a = [float(i) for i in input().split()]
print("Среднее арифметическое данного массива равно",numpy.mean(a))

#Написать две функции, которые будут переводить из десятичной СС в двоичную и обратно.

def bin_to_dec(dig):
    dl=len(dig)
    ch_dec=0
    for i in range(0, dl):
        ch_dec=ch_dec+int(dig[i])*(2**(dl-i-1))
    return ch_dec
print("Введите двоичное целое число")
b=input()
print("Двоичное целое число", b, "соответствует десятичному числу", bin_to_dec(b))

print("Введите десятичное целое число")
n=int(input())
m=n
c=''
while n>0:
    c= str(n%2)+c
    n=n//2
print("Десятичное число", m,"соответствует двоичному числу", c)

#Пользователь делает вклад в размере a рублей сроком на years лет под 10% годовых (каждый год размер его вклада увеличивается на 10%. Эти деньги прибавляются к сумме вклада, и на них в следующем году тоже будут проценты).
#Написать функцию bank, принимающая аргументы a и years, и возвращающую сумму, которая будет на счету пользователя.

def bank():
    profit=0.1
    print("Какую сумму пользователь вкладывает в банк?")
    a1=int(input())
    print("На сколько лет пользователь открывает счет?")
    years=int(input())
    d=a1*(1+profit)**years
    print("По итогу пользователь получает", d, "рублей")
bank()

#Даны четыре действительных числа: x1, y1, x2, y2. Напишите функцию distance(x1, y1, x2, y2), вычисляющая расстояние между точкой (x1,y1) и (x2,y2). Считайте четыре действительных числа и выведите результат работы этой функции.

from math import sqrt
def distance(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
print("Введите координаты точек")
x1 = float(input())
x2 = float(input())
y1 = float(input())
y2 = float(input())
print("Расстояние между точками равно", distance(x1, x2, y1, y2))

#Дано действительное положительное число a и целоe число n.
#Вычислите a^n. Решение оформите в виде функции power(a, n).
#Стандартной функцией возведения в степень пользоваться нельзя.
#Учтитье, что n может быть отрицательным.

def power(a2, n2):
    res=1
    for i in range(abs(n2)):
        res*=a2
    if n2>=0:
        return res
    else:
        return 1/res
print("Введите основание и показатель степени")
print(power(float(input()), int(input())))

#Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000, и возвращающую True, если оно простое, и False - иначе.

from math import sqrt
def is_prime(num):
    if num%2==0 and num!=2:
        return False
    if num==0 or num==1:
        return False
    for n3 in range(3, int(sqrt(num).real) + 1, 2):
        if num%n3==0:
            return False
    return True
print("Введите число от 0 до 1000")
n3=int(input())
print(is_prime(n3))