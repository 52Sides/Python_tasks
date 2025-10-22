"""
Задача:
Вам дается текстовый файл, содержащий некоторое количество непустых строк.
На основе него сгенерируйте новый текстовый файл, содержащий те же строки в обратном
порядке.

Пример входного файла:
ab
c
dde
ff

Пример выходного файла:
ff
dde
c
ab
"""

with open("5.8. input.txt", "r") as f, open("5.8. result.txt", "w") as w:
	for i in [i for i in f.read().split()][::-1]:
		w.write(str(i) + "\n")
	w.close()


# оптимизация предыдущего
print(*reversed(open("5.8. input.txt").readlines()), sep="")

