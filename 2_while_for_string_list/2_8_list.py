"""
Задача:
Напишите программу, на вход которой подается одна строка с целыми числами.
Программа должна вывести сумму этих чисел. Используйте метод split строки.

Sample Input:
4 -1 9 3
Sample Output:
15
"""

x = [i for i in input().split()]
a = int()

for i in x:
    a += int(i)

print(a)


# Или так:
print(sum([int(i) for i in input().split()]))