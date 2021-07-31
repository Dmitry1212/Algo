# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
import random
from functools import reduce

num = 5

matrix = [[random.randint(0, num) for _ in range(num)] for _ in range(num)]

for line in matrix:
    for item in line:
        print(f'{item:>4}', end='')
    print()

print('-' * 30)

# ищем минимальные элементы в столбцах
min = matrix[0]
for line in matrix:
    for i, item in enumerate(line):
        if min[i] > item:
            min[i] = item

print(f'Максимальный элемент из минимальных в столцах равен: {reduce(lambda a, b: a if (a > b) else b, min)}')
