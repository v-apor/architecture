class Point:

    def __init__(self, x, y):
        self.move(x, y)

    def move(self, x, y):
        self.x = x
        self.y = y

    def reset(self):
        self.move(0,0)

    def calculate_distance(self, other_point):
        return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)

a = Point(2, 5)
print(a.x, a.y)

# The line below throws error b'cos 2 arguments required to create object (cos of __init__)
# b = Point()