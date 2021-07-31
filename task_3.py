# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random

mas = [random.randint(0, 100) for _ in range(10)]
print(f'исходный массив: \n{mas}\n', '*'*len(mas))


# поиск максимума и минимума
min1 = mas[0]
max1 = mas[0]
maxi = 0
mini = 0

for i, item in enumerate(mas):
    if min1 > item:
        min1 = item
        mini = i
    if max1 < item:
        max1 = item
        maxi = i

# вывод инфо
print(f'Найдено: \n - минимум {min1} в позиции {mini},\n - максимум {max1} в позиции {maxi}')

if mini < maxi:
    print(f'{mas[:mini]}\033[34m {mas[mini]} \033[0m {mas[mini+1:maxi]} \033[31m {mas[maxi]} \033[0m {mas[maxi+1:]} ')
else:
    print(f'{mas[:maxi]}\033[34m {mas[maxi]} \033[0m {mas[maxi+1:mini]} \033[31m {mas[mini]} \033[0m {mas[mini+1:]} ')

# перестановка
mas[mini], mas[maxi] = mas[maxi], mas[mini]
print('меняем местами:')
if mini < maxi:
    print(f'{mas[:mini]}\033[34m {mas[mini]} \033[0m {mas[mini+1:maxi]} \033[31m {mas[maxi]} \033[0m {mas[maxi+1:]} ')
else:
    print(f'{mas[:maxi]}\033[34m {mas[maxi]} \033[0m {mas[maxi+1:mini]} \033[31m {mas[mini]} \033[0m {mas[mini+1:]} ')

