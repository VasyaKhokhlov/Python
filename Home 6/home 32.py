"""Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
(т.е. не меньше заданного минимума и не больше заданного максимума)
"""

import random 
n = int(input('Введите размер массива: '))
arr = []
min_number = int(input())
max_number = int(input())
for i in range(n):
    arr.append(random.randrange(n))
print(arr)
for i in range(len(arr)):
        if min_number <= arr[i] <= max_number:
         print(i, end='')





