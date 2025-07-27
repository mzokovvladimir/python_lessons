from collections import namedtuple


my_tuple = (1, 2, 3)
print(my_tuple)
print(type(my_tuple))
# my_tuple[0] = 50
# print(my_tuple)

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p)
print(type(p))
print(p[1])
print(p[:1])
print(3 in p)
print(3 not in p)
print(p.x)
print(p.y)
data = [10, 20]
point = Point._make(data)
print(point)
new_point = point._replace(y=50)
print(new_point)