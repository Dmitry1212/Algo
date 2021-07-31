# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать

import random
from functools import reduce

num = 10
mas = [random.randint(-num, num) for _ in range(20)]
print(f'исходный массив: \n{mas}\n', '*' * len(mas) * 4)

# ищем максимум
max1 = mas[0]
min1 = mas[0]
for i in mas:
    if max1 < i:
        max1 = i
    elif min1 > i:
        min1 = i

# print(min1, max1)

if mas.index(min1) < mas.index(max1):
    mas_sum = mas[mas.index(min1) + 1:mas.index(max1)]
else:
    mas_sum = mas[mas.index(max1) + 1:mas.index(min1)]
# print(mas_sum)

sum_all = reduce(lambda x, y: x + y, mas_sum)
print(f'Сумма элементов между максимальным и минимальными элементами = {sum_all}')
