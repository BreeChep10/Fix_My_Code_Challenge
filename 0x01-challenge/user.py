#!/usr/bin/python3

class Square():

    def __init__(self, width=0, height=0, **kwargs):
        self.width = width
        self.height = height
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """Area of the square"""
        return self.width * self.width

    def perimeter_of_my_square(self):
        return self.width * 4  # Perimeter for a square is 4 times the side length

    def __str__(self):
        return f"Square: {self.width} x {self.height}"

if __name__ == "__main__":
    s = Square(width=12, height=12)
    print(s)
    print("Area:", s.area_of_my_square())
    print("Perimeter:", s.perimeter_of_my_square())
