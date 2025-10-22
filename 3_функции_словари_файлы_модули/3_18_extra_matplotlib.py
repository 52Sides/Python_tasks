from pylab import *

x = linspace(0, 5, 10)
y = x ** 2
print(x)
print(y)

figure()
plot(x, y, 'r')
xlabel('x')
ylabel('y')
title('title')
show()

fig = plt.figure()

axes = fig.add_axes([0.1, 0.1, 0.3, 0.3])  # Относительно положения на картинке
axes.plot(x, y, 'r')  # Значения и стиль построения графика
axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_title('title')  # Чтобы не отображалась строка <matplotlib...

# Рисование сразу двух графиков
fig = plt.figure()

axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3])


# main figure
axes1.plot(x, y, 'r')
axes1.set_xlabel('x')
axes1.set_ylabel('y')
axes1.set_title('title')


# insert
axes2.plot(y, x, 'g')
axes2.set_xlabel('x')
axes2.set_ylabel('y')
axes2.set_title('insert title')


# можно нарисовать два графика раздельно
fig, axes = plt.subplots(nrows = 1, ncols = 2)

for ax in axes:
    ax.plot(x, y, 'r')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('title')

fig.tight_layout() # делает так, чтобы графики не пересекались
fig, axes = plt.subplots(figsize=(12,3)) # позволяет задать размеры графика (в дюймах)


# совмещенные графики на одном поле с легендой
fig, ax = plt.subplots()

ax.plot(x, x**2, label="y = x ** 2")
ax.plot(x, x**3, label="y = x ** 3")
ax.legend(loc=2); #upper left corner
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('title')


#Построение гистограммы
from numpy import *

n = random.randn(100000) # функция из numpy
fig, axes = plt.subplots(1, 2, figsize=(12,4))

axes[0].hist(n)
axes[0].set_title('default histogram')
axes[0].set_xlim((min(n), max(n)))

axes[1].hist(n, cumulative=True, bins=50)
axes[1].set_title('cumulative detailed histogram')
axes[1].set_xlim((min(n), max(n)))
