import math

class Point:

    def move(self, x, y):
        self.x = x
        self.y = y

    def reset(self):
        self.move(0,0)

    def calculate_distance(self, other_point):
        return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)

a = Point()
a.reset()

b = Point()
b.move(2, 2)

print(a.calculate_distance(b))

# This is to test if a->b == b->a
if assert(a.calculate_distance(b) == b.calculate_distance(a)):
    print("Success")
# will get assert error for below calse
# assert(a.calculate_distance(b) == 4)
