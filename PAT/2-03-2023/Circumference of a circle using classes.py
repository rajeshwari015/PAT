"""write a program that has a class circle
use a class variable defining pi constant
use the class variabel to claculate the area and circumference with radius 7.5"""
import math
import time
start=time.time()
class Circle:
    def __init__(self,r):
        self.r=r
    def area(self):
        print("The area is",math.pi*self.r*self.r)
    def circumference(self):
        print("The circumference is",2*math.pi*self.r)

        
x=Circle(7.5)
x.area()
x.circumference()
end=time.time()
print(end-start)
