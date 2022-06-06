import math


class Polyhedron:
    def __init__(self, a, b, h, r):
        self.h = h
        self.a = a
        self.b = b
        self.r = r

        # Basic parameters
        self.base_area = a * b
        self.lateral_surface_area = 2 * (a * h) + 2 * (b * h)
        self.circuit_base_area = 2 * a + 2 * b


    def total_area(self):
        print('Total area of polyhedron:', 2 * self.base_area + self.lateral_surface_area)


    def total_lateral_surface_area(self):
        print('Total lateral surface area of polyhedron:', self.circuit_base_area * self.h)


    def total_volume(self):
        print('Total volume of polyhedron:', self.base_area * self.h)


    def f_circuit_base_area(self):
        print('Circuit base area of polyhedron:', self.circuit_base_area)


class Cylinder(Polyhedron):
    def __init__(self, *args):
        super().__init__(*args)


    def c_circuit_base_area(self):
        print('Circuit base area of cylinder:', round(2 * math.pi * self.r, 2))


    def c_base_area(self):
        print('Base area of cylinder:', round(2 * math.pi * (self.r ** 2), 2))


x = int(input('Enter first edge of base: '))
y = int(input('Enter second edge of base: '))
high = int(input('Enter high of polyhedron: '))
radius = int(input('Enter radius of cylinder or cuboid: '))

Cylinder1 = Cylinder(x, y, high, radius)
Cylinder1.c_circuit_base_area()
