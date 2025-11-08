'''
Create class Circle with attribute radius

add methods area() and circumference()
use math module for pi value
'''
from math import pi
class Circle:
    def __init__(self, radius):
        self.radius=radius

    def area(self):
        print(f' Radius : {pi * self.radius *self.radius}')

    def circumference(self):
        print(f"Circumference : {2 * pi * self.radius}")

c=Circle(100)
c.area()
c.circumference()


