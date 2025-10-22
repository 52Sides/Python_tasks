"""
Задача:
Вашей программе на вход подаются две строки s и t, состоящие из строчных латинских букв.
Выведите одно число – количество вхождений строки t в строку s. (c пересечениями)
Пример:
s = "abababa"
t = "aba"

Sample Input 1:
abababa
aba
Sample Output 1:
3

Sample Input 2:
abababa
abc
Sample Output 2:
0

Sample Input 3:
abc
abc
Sample Output 3:
1

Sample Input 4:
aaaaa
a
Sample Output 4:
5
"""

n, (s, t) = 0, (input() for _ in range(2))

while s != '':
    if s.startswith(t):
        n += 1

    s = s.replace(s[0],s[0].upper(),1)
    s = s.strip(s[0])

print(n)


# оптимизация предыдущего
n, s, t = 0, input(), input()

for i in range(len(s)):
    if s[i:].startswith(t):
        n += 1

print(n)

