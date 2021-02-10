class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def rectangle_area(self):
        return self.width*self.length


r1 = Rectangle(5, 10)
print(r1.rectangle_area())