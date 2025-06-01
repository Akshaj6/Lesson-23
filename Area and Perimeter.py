import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        circle_area = math.pi * (self.radius ** 2)
        return circle_area
    def perimeter(self):
        circle_perimeter = 2 * math.pi * self.radius
        return circle_perimeter
radius = int(input("Enter a radius for the circle :\n"))
my_circle = Circle(radius)
calculated_area = my_circle.area()
print("The area of the circle is :", calculated_area)
calculated_perimeter = my_circle.perimeter()
print("The perimeter of the circle is :", calculated_perimeter)