import math


## without exception handling
class Circle(object):
    def __init__(self, radius1):
        self.radius = radius1  # Private Attribute

    def print_circle_area(self):
        result = 2 * math.pi * self.radius
        print('Circle area: {}'.format(round(result, 2)))


circle1 = Circle(3)
circle1.print_circle_area()


## with exception handling
# class Circle(object):
#     def __init__(self, radius1):
#         try:
#             self.radius = radius1  # Private Attribute
#         finally:
#             print('Invalid input!')
#
#     def print_circle_area(self):
#         result = 2 * math.pi * self.radius
#         print('Circle area: {}'.format(round(result, 2)))
#
#
# circle1 = Circle('a')
# circle1.print_circle_area()
