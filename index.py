from math import pi, sqrt


class Figure:

    def __init__(self, name, sideA, angles=4):
        self.name = name
        self.angles = angles
        self.sideA = sideA

    @property
    def perimeter(self):
        return self.sideA * self.angles

    @property
    def area(self):
        return self.sideA * self.sideA

    def add_square(self, obj):
        try:
            return obj.perimeter + self.perimeter
        except AttributeError:
            return "Argument must be instance of Figure class"


class Rectangle(Figure):
    def __init__(self, name, sideA, sideB, angles=4):
        super().__init__(name, sideA, angles)
        self.sideB = sideB

    @property
    def area(self):
        return self.sideA * self.sideB

    @property
    def perimeter(self):
        return (self.sideA + self.sideB) * 2


class Triangle(Rectangle):
    def __init__(self, name, sideA, sideB, sideC, angles=3):
        super().__init__(name, sideA, sideB, angles)
        self.sideC = sideC

    @property
    def perimeter(self):
        return self.sideA + self.sideB + self.sideC

    @property
    def area(self):
        s = (self.sideA + self.sideB + self.sideC) / 2
        return sqrt(s * (s - self.sideA) * (s - self.sideB) * (s - self.sideC))


class Circle(Figure):
    def __init__(self, name, sideA):
        super().__init__(name, sideA)
        self.sideA = sideA

    @property
    def area(self):
        return pi * self.sideA ** self.sideA

    @property
    def perimeter(self):
        return 2 * pi * self.sideA
