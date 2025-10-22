"""
Задача:
Вам дано описание наследования классов в формате JSON.
Описание представляет из себя массив JSON-объектов, которые соответствуют классам.
У каждого JSON-объекта есть поле name, которое содержит имя класса, и поле parents,
которое содержит список имен прямых предков.

Пример:
[
{"name": "A", "parents": []},
{"name": "B", "parents": ["A", "C"]},
{"name": "C", "parents": ["A"]}
]

Эквивалент на Python:
class A:
    pass
class B(A, C):
    pass
class C(A):
    pass

Гарантируется, что никакой класс не наследуется от себя явно или косвенно, и что
никакой класс не наследуется явно от одного класса более одного раза. Для каждого класса
вычислите предком скольких классов он является и выведите эту информацию в следующем
формате: <имя класса> : <количество потомков>

Выводить классы следует в лексикографическом порядке.
Sample Input:
[
{"name": "A", "parents": []},
{"name": "B", "parents": ["A", "C"]},
{"name": "C", "parents": ["A"]}
]

[
{"name": "B", "parents": ["A", "C"]},
{"name": "C", "parents": ["A"]},
{"name": "A", "parents": []}
]

[
{"name": "B", "parents": ["AD", "CA"]},
{"name": "C", "parents": ["AA"]},
{"name": "AA", "parents": []}
]

Sample Output:
A : 3
B : 1
C : 2
"""

import json

d = {}
dicts = json.loads(input())

for i in dicts:
    if i['name'] not in d:
        d.get(i['name'])
        d[i['name']] = ['object']

for i in dicts:
    for j in i['parents']:
        d[j] += [i['name']]

for key1 in d.keys():
    for key2 in d.keys():
        if key1 in d[key2]:
            d[key2] += d[key1]

for key in sorted(d):
    print(key, ":", len(set(d[key])))


# Вариация через рекурсию
def child_counter(name):
    for key in d.keys():
        if name in d[key]:
            s.add(key)
            child_counter(key)
    return str(len(s)+1)

d = {dicts['name']: dicts['parents'] for dicts in json.loads(input())}

for key in sorted(d):
    s = set()
    print(key, ":", child_counter(key))
