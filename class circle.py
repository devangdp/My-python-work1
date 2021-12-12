from math import pi
class circle:
    def __init__(self, a, b, r):
        self.a=a
        self.b=b
        self.r=r

    def Area(self):
        return pi * self.r**2

    def Perimeter(self):
        return 2 * pi * self.r
 
c1=circle(5,6,3)

print('Perimeter :', c1.Perimeter())
print('Area :', c1.Area())
print('Perimeter :', '{:.2f}'.format(c1.Perimeter()))
print('Area :', '{:.2f}'.format(c1.Area()))
