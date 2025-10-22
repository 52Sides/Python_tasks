"""
Задача:
В первой строке дано три числа, соответствующие некоторой дате date - год, месяц и день.
Во второй строке дано одно число days -- число дней.
Вычислите и выведите год, месяц и день даты, которая наступит, когда с момента исходной
даты date пройдет число дней, равное days.

Примечание:
Для решения этой задачи используйте стандартный модуль datetime.
Вам будут полезны класс datetime.date для хранения даты и класс datetime.timedelta
для прибавления дней к дате.

Sample Input 1:
2016 4 20
14
Sample Output 1:
2016 5 4

Sample Input 2:
2016 2 20
9
Sample Output 2:
2016 2 29

Sample Input 3:
2015 12 31
1
Sample Output 3:
2016 1 1
"""

import datetime

a = [int(i) for i in input().split()]
a = datetime.date(a[0], a[1], a[2]) + datetime.timedelta(days=int(input()))
print(str(a.year) + ' ' + str(a.month) + ' ' + str(a.day))


# оптимизация предыдущего
d = datetime.date(*map(int, input().split())) + datetime.timedelta(days=int(input()))
print(d.year, d.month, d.day)