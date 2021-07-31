# 7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой
# (оба минимальны), так и различаться.

import random
from functools import reduce

num = 10
mas = [random.randint(0, num) for _ in range(10)]
print(f'исходный массив: \n{mas}\n', '*' * len(mas) * 4)

min1 = reduce(lambda a, b: a if (a < b) else b, mas)
print(min1)

mas2 = mas[:mas.index(min1)] + mas[mas.index(min1) + 1:]
min2 = reduce(lambda a, b: a if (a < b) else b, mas2)
print(f'Минимальные значения: {min1} и {min2}')
