import math

class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        return self.width * self.height

    def __eq__(self, other):
        return self.get_square() == other.get_square()

    def __add__(self, other):
        newwidth = self.width + other.width
        return Rectangle(newwidth,(self.get_square() + other.get_square()) / newwidth)

    def __mul__(self, n):
        newsquare = self.get_square() * n
        newwidth = self.width + math.isqrt(self.width)
        newheight = newsquare / newwidth
        return Rectangle(newwidth,newheight)

    def __str__(self):
        return "width: " + str(self.width) + ", height: " +  str(self.height) + ", square: " + str(self.get_square())


r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)
print(r1.get_square() == 8)
print(r2.get_square() == 18)

r3 = r1 + r2
print(r3.get_square() == 26)
print(str(r3))

r4 = r1 * 4
print(r4.get_square() == 32)
print(str(r4))


print(Rectangle(3, 6) == Rectangle(2, 9))
