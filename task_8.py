# 8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

from functools import reduce

ni = 5
nj = 4

matrix = []

print('Введите значения матрицы: ')
for i in range(ni):
    line = []
    for j in range(nj):
        line.append(int(input('next ')))
    line.append(reduce(lambda x, y: x + y, line))
    matrix.append(line)

for line in matrix:
    for item in line:
        print(f'{item:>4}', end='')
    print()
