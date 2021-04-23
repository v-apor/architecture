# Note that in python we can even assign attributes to an object
# even if it isn't declared in class

class Point:
    pass

a = Point()
a.x = 2
a.y = 4

b = Point
b.x = 3
b.y = 6

print(a.x, a.y)
print(b.x, b.y)