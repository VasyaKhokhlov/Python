"""Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

*Пример:*

A = 3; B = 5 -> 243 (3⁵)
    A = 2; B = 3 -> 8 
"""
n = int(input( ' Введите число: '))
s = int(input( ' Введите степень числа: '))
def stepen( n, s ) :
    if s == 0 :
        return 1
    else:
        return n * stepen ( n, s - 1)
print (stepen( n, s ))
