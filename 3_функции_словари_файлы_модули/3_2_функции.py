"""
Задача:
Напишите функцию modify_list(l), которая принимает на вход список целых чисел, удаляет
из него все нечётные значения, а чётные нацело делит на два.

Функция не должна ничего возвращать, требуется только изменение переданного списка,
например:
lst = [1, 2, 3, 4, 5, 6]
print(modify_list(lst))  # None
print(lst)               # [1, 2, 3]
modify_list(lst)
print(lst)               # [1]

lst = [10, 5, 8, 3]
modify_list(lst)
print(lst)               # [5, 4]

Функция не должна осуществлять ввод/вывод информации.
"""

def modify_list(l):
    for i in l[::-1]:
        if i % 2 != 0:
            l.remove(i)

    for i in range(len(l)):
        l[i] = l[i] // 2


#Или так:
l = [int(i) for i in input().split()]

def modify_list_2(l):
    l[:] = [i // 2 for i in l if i % 2 == 0]