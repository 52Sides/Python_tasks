"""
Задача:
Простейшая система проверки орфографии может быть основана на использовании списка
известных слов.

Если введённое слово не найдено в этом списке, оно помечается как "ошибка".
Попробуем написать подобную систему.
На вход программе первой строкой передаётся количество d известных нам слов,
после чего на d строках указываются эти слова.
Затем передаётся количество l строк текста для проверки, после чего l строк текста.
Выведите уникальные "ошибки" в произвольном порядке. Работу производите без учёта
регистра.

Sample Input:
4
champions
we
are
Stepik
3
We are the champignons
We Are The Champions
Stepic
Sample Output:
stepic
champignons
the
"""

a = [input().lower() for i in range(int(input()))]
text = [str(input()).lower().split() for i in range(int(input()))]
errors = set()

for i in text:
    for j in range(len(i)):
        if i[j] not in a:
            errors.add(i[j])

print(*errors, sep = '\n')