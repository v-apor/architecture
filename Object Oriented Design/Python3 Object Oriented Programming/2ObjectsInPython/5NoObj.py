class Point:

    def move(self, x, y):
        self.x = x
        self.y = y

    def reset(self):
        self.move(0,0)

    def calculate_distance(self, other_point):
        return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)

a = Point()
a.x = 2

print(a.x)
# The line below throws exception:
# print(a.y)