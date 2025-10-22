"""
Задача:
Вам дано описание пирамиды из кубиков в формате XML.
Кубики могут быть трех цветов: красный (red), зеленый (green) и синий (blue).
Для каждого кубика известны его цвет, и известны кубики, расположенные прямо под ним.

Пример:
<cube color="blue">
  <cube color="red">
    <cube color="green">
    </cube>
  </cube>
  <cube color="red">
  </cube>
</cube>

Введем понятие ценности для кубиков. Самый верхний кубик, соответствующий корню XML
документа имеет ценность 1. Кубики, расположенные прямо под ним, имеют ценность 2.
Кубики, расположенные прямо под нижележащими кубиками, имеют ценность 3. И т. д.
Ценность цвета равна сумме ценностей всех кубиков этого цвета. Выведите через пробел
три числа: ценности красного, зеленого и синего цветов.

Sample Input:
<cube color="blue"><cube color="red"><cube color="green"></cube></cube><cube color="red"></cube></cube>
Sample Output:
4 3 1
"""

import xml.etree.ElementTree as ET

def give_value(root, value):
    for i in range(len(root)):
        root[i].attrib.update({str('value'): value})
        give_value(root[i], value + 1)

root = ET.fromstring(input())
root.attrib.update({str('value'): 1})

give_value(root, 2)

red, green, blue = 0, 0, 0

for i in root.iter():
    if i.attrib["color"] == 'blue':
        blue += i.attrib['value']

    if i.attrib["color"] == 'red':
        red += i.attrib['value']

    if i.attrib["color"] == 'green':
        green += i.attrib['value']

print(red, green, blue)


# оптимизация предыдущего
from xml.etree import ElementTree

root = ElementTree.fromstring(input())
colors = {"red": 0, "green": 0, "blue": 0}

def get_cubes(root, value):
    colors[root.attrib['color']] += value
    for child in root:
        get_cubes(child, value+1)

get_cubes(root,1)
print(colors["red"], colors["green"], colors["blue"])