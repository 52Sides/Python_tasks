"""
Задача:
Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего
файла. Первое слово в тексте последнего файла: "We".

Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора.

Все файлы располагаются в каталоге по адресу:
https://stepik.org/media/attachments/course67/3.6.3/

Загрузите содержимое последнего файла из набора, как ответ на это задание.
"""

import requests

BASE_URL = 'https://stepik.org/media/attachments/course67/3.6.3/'
FILE_URL = '699991.txt'

while True:
    if FILE_URL.find("We") == 0:
        break
    url = requests.get(BASE_URL + FILE_URL).text
with open('result_task_4.txt', 'w') as data:
    data.write(FILE_URL)


#Или так:
import requests

url, name = 'https://stepik.org/media/attachments/course67/3.6.3/', '699991.txt'

while name[:2] != 'We':
    name = requests.get(url + name).text

print(name)
