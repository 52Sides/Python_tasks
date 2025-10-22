"""
Задача:
Вашей программе на вход подаются три строки s, a, b, состоящие из строчных латинских
букв. За одну операцию вы можете заменить все вхождения строки a в строку s на строку b.

Например, s = "abab", a = "ab", b = "ba", тогда при 1 операции s = "baba",
после 2 операции  s = "bbaa", и дальнейшие операции не смогут изменять строку s.

Необходимо узнать, после какого минимального количества операций в строке s не останется
вхождений строки a. Если операций потребуется более 1000, выведите Impossible.

Выведите одно число – минимальное число операций, после применения которых в строке s
не останется вхождений строки a, или Impossible, если операций потребуется более 1000.

Sample Input 1:
ababa
a
b
Sample Output 1:
1

Sample Input 2:
ababa
b
a
Sample Output 2:
1

Sample Input 3:
ababa
c
c
Sample Output 3:
0

Sample Input 4:
ababac
c
c
Sample Output 4:
Impossible
"""

s, a, b, n = input(), input(), input(), 0

while a in s:
    if n == 1000:
        n = "Impossible"
        break

    else:
        s = s.replace(a,b)
        n += 1

print(n)

