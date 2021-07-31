# 4. Определить, какое число в массиве встречается чаще всего.
import random

num = 10
mas = [random.randint(0, num) for _ in range(20)]
print(f'исходный массив: \n{mas}\n', '*' * len(mas))

frec = {mas[0]: 0}
print()

for pos, i in enumerate(mas):
    fl = True
    for j, item in enumerate(frec):
        if i == item:
            frec[i] += 1
            fl = False
            continue
    if fl:
        frec[mas[pos]] = 1

print(frec)
