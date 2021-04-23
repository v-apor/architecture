class Point:
    # Note: for every method(of class) one parameter is essential (not needed in function, outside class)
    def reset(self):
        self.x = 0
        self.y = 0

a = Point()
a.x = 2
a.y = 4

print(a.x, a.y)
a.reset()
print(a.x, a.y)

# We can also call metod from class but have to pass object as argument(for self)
a.x = 2
a.y = 4
print(a.x, a.y)
# See here, calling method from class name but passing object as arg for self
Point.reset(a)
print(a.x, a.y)