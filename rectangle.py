class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y

    def perimeter(self):
        return self.x + self.y + self.y + self.x

Rectangle = Rectangle(x=4, y=6)


print("Area:", Rectangle.area())
print("Perimeter:", Rectangle.perimeter())


