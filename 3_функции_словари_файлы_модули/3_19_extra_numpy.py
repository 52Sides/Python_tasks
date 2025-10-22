from numpy import *

a = array([2, 3, 4])  #создание одномерного массима из списка целых чисел
print(a)
print("a.ndim:" + str(a.ndim))
print("a.shape:" + str(a.shape))

b = array([(1.5, 2, 3), (4, 5, 6)])
print(b)
print("b.ndim:" + str(b.ndim))
print("b.shape:" + str(b.shape))

c = zeros((3,5))
print(c)
print(arange(5,10,1))
print(linspace(0, 2, 9))

b = arange(12).reshape(6, 2)
print(b)

2 * sin(a)