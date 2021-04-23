class Point:

    def __init__(self, x=0, y=0):
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

# This time no error because of default args provided in args
b = Point()
print(b.x, b.y)