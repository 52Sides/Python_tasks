"""
Задача:
Рассмотрим два HTML-документа A и B. Из A можно перейти в B за один переход, если
в A есть ссылка на B, т. е. внутри A есть тег <a href="B">, возможно с дополнительными
параметрами внутри тега.

Из A можно перейти в B за два перехода если существует такой документ C, что из A в C
можно перейти за один переход и из C в B можно перейти за один переход.

Вашей программе на вход подаются две строки, содержащие url двух документов A и B.
Выведите Yes, если из A в B можно перейти за два перехода, иначе выведите No.

Обратите внимание на то, что не все ссылки внутри HTML документа могут вести на
существующие HTML документы.

Sample Input 1:
https://stepik.org/media/attachments/lesson/24472/sample0.html
https://stepik.org/media/attachments/lesson/24472/sample2.html
Sample Output 1:
Yes
Sample Input 2:
https://stepik.org/media/attachments/lesson/24472/sample0.html
https://stepik.org/media/attachments/lesson/24472/sample1.html
Sample Output 2:
No
Sample Input 3:
https://stepik.org/media/attachments/lesson/24472/sample1.html
https://stepik.org/media/attachments/lesson/24472/sample2.html
Sample Output 3:
Yes
"""

import re
import requests

a = input()
b = list(input())
b.append(b[0].replace("stepik.org", "stepic.org"))

a = str(requests.get(a).content)
a = re.findall(r"http.+?html", a)

list_c = []

for i in a:
    text = str(requests.get(i).content)
    text = re.findall(r"http.+?html", text)
    list_c += text

print(["No","Yes"][any(i in b for i in list_c)])

# регулярка поиска html ссылок
# link_pattern = re.compile(r'<a[^>]*?href="(.*?)"[^>]*?>')

