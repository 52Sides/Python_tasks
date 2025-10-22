"""
Задача:
Вам дана в архиве файловая структура, состоящая из директорий и файлов. Вам необходимо
распаковать этот архив, и затем найти в данной в файловой структуре все директории,
в которых есть хотя бы один файл с расширением ".py".

Ответом на данную задачу будет являться файл со списком таких директорий,
отсортированных в лексикографическом порядке. Для лучшего понимания формата задачи,
ознакомьтесь с примером.

Пример ответа
sample
sample/a
sample/a/c
sample/b
"""

import os.path

py_dir_list = []

for current_dir, dirs, files in os.walk("main"):
    for i in files:
        if i.split(".")[1] == "py":
            py_dir_list.append(current_dir)

py_dir_list = sorted(set(py_dir_list))

with open("5.9. result.txt", 'w') as w:
    for i in py_dir_list:
        w.write(str(i) + "\n")


# Или так:
import zipfile, os

dirs = list()

with zipfile.ZipFile('5.9. main.zip', 'r') as zip:
    for zip_path in zip.namelist():
        if os.path.dirname(zip_path) not in dirs:
            if os.path.basename(zip_path).endswith('.py'):
                dirs.append(os.path.dirname(zip_path))

print('\n'.join(sorted(dirs)))