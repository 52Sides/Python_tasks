"""
Задача:
В этой задаче вам необходимо воспользоваться API сайта numbersapi.com
Вам дается набор чисел. Для каждого из чисел необходимо узнать, существует ли
интересный математический факт об этом числе.

Для каждого числа выведите Interesting, если для числа существует интересный факт,
и Boring иначе. Выводите информацию об интересности чисел в таком же порядке, в каком
следуют числа во входном файле.

Пример запроса к интересному числу:
http://numbersapi.com/31/math?json=true
Пример запроса к скучному числу:
http://numbersapi.com/999/math?json=true

Пример входного файла:
31
999
1024
502

Пример выходного файла:
Interesting
Boring
Interesting
Boring
"""

import requests
import sys
import json

for num in sys.stdin:
    num = str(num.rstrip())
    res = requests.get(f"http://numbersapi.com/{num}/math?json=true")
    print(["Interesting", "Boring"][res.json()['found'] == False])


# вариант через респонс
for num in sys.stdin:
    pattern = 'http://numbersapi.com/{number}/math?json=true'
    response = requests.get(pattern.format(number=num.rstrip())).json()
    print('Interesting' if response['found'] else 'Boring')