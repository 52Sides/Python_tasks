"""
Задача:
Выведите таблицу размером n×n, заполненную числами от 1 до n**2 по спирали, выходящей
из левого верхнего угла и закрученной по часовой стрелке, как показано в примере
(здесь n=5):

Sample Input:
5
Sample Output:
1 2 3 4 5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9
"""

a = int(input())
m = [[int(0) for j in range(a)] for i in range(a)]
m[0][0] += 1
last = 1

while last < a*a:
    for i in range(a):
        for j in range(a):
            if m[i][j] == last:
                if j < a-1 and m[i][j+1] == 0:
                    for aj in range(j+1, a):
                        if m[i][aj] == 0:
                            m[i][aj] = last + 1
                            last = last + 1

                elif i < a-1 and m[i+1][j] == 0 :
                    for ai in range(i+1, a):
                        if m[ai][j] == 0:
                            m[ai][j] = last + 1
                            last = last + 1

                elif j > 0 and m[i][j-1] == 0:
                    for aj in range(j-1, -1, -1):
                        if m[i][aj] == 0:
                            m[i][aj] = last + 1
                            last = last + 1

                elif i > 0 and m[i-1][j] == 0:
                    for ai in range(i-1, -1, -1):
                        if m[ai][j] == 0:
                            m[ai][j] = last + 1
                            last = last + 1

[print(*g) for g in m]


#Или так:
a = int(input())
m = [[int(0) for j in range(a)] for i in range(a)]
s, k = 0, 1

while k <= a*a:
    for i in range(s, a-s, 1):  # Заполнение вправо (по столбцам) до упора в смещение
        m[s][i] = k; k += 1

    for i in range(s+1, a-s, 1):  # Заполнение вниз (по строчкам) до упора в смещение
        m[i][(a-1)-s] = k; k += 1

    for i in range(a-s-2, s-1, -1):  # Заполнение влево (по столбцам) до упора в смещение
        m[a-s-1][i] = k; k += 1

    for i in range(a-s-2, s, -1):  # Заполнение вверх (по строчкам) до упора в смещение
        m[i][s] = k; k += 1

    s += 1  # Увеличиваем смещение после каждого цикла

[print(*line) for line in m]