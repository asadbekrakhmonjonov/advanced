class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def __str__(self):
        return f'rectangle {self.length}x{self.width}'

class Square(Rectangle):
    def __init__(self, length: int):
        # Call the __init__ method of the parent class using super()
        super().__init__(length, length)

    # No need for a separate square method, as it's essentially the same as the area method in the parent class.

    def __str__(self):
        return f'square {self.length} x {self.length}'

if __name__ == "__main__":
    rectangle = Rectangle(2, 3)
    print(rectangle)
    print("area:", rectangle.area())

    square = Square(4)
    print(square)
    print("area:", square.area())
