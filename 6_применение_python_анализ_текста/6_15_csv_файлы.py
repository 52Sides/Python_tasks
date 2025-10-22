"""
Задача:
Вам дана частичная выборка из датасета зафиксированных преступлений, совершенных в
городе Чикаго с 2001 года по настоящее время.
Одним из атрибутов преступления является его тип – Primary Type.
Вам необходимо узнать тип преступления, которое было зафиксировано максимальное число
раз в 2015 году.

Файл с данными:
Crimes.csv
"""

import csv

d = {}

with open("6.15. сrimes.csv", "r") as data:
    csv_content = csv.reader(data)

    for i in csv_content:
        if "2015" in i[2]:
            if i[5] not in d:
                d[i[5]] = 0
            d[i[5]] += 1

for key in d.keys():
    if max(d[key] for key in d.keys()) == d[key]:
        print(key)


# вариация через lst
import csv

lst = []

with open("6.15. сrimes.csv", "r") as data:
    csv_content = csv.reader(data)

    for i in csv_content:
        if "2015" in i[2]:
            lst.append(i[5])

print(max(lst, key=lst.count))
