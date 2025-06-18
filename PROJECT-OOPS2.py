import math
class circle:
    def __init__(self,r):
        self.radius=float(r)
    def c_area(self):
        return math.pi*(self.radius*self.radius)
newCircle=circle(input("enter radius for circle: "))
print("Area of this circle is ",round(newCircle.c_area(),3),"units sq.")