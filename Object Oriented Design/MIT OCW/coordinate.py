class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y 

    def __str__(self):
        return f"<{self.x},{self.y}>"

    def __add__(self, other):
        return (self.x + other.x, self.y + other.y)

    def distance(self, other):
        x_diff_sq = (self.x - other.x)**2
        y_diff_sq = (self.y - other.y)**2
        return (x_diff_sq+y_diff_sq)**.5

c = Coordinate(3, 4)
d = Coordinate(1, 1)
origin = Coordinate(0, 0)
# print(c.x)
# print(origin.x)
# print(c.distance(origin))
print(c)
# print(c.__add__(d))
print(c + d)