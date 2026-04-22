class Shapes:
    def area(self):
        print("The area is:")
class Rectangle(Shapes):
        def __init__(self,l,b):
             self.l=l
             self.b=b
        def area(self):
             print("The area of reactangle:",self.l*self.b)
class Square(Shapes):
        def __init__(self,s):
             self.s=s
        def area(self):
             print("The area of square:",self.s*self.s)
l=int(input("Enter the length of rectangle:"))
b=int(input("Enter the breadth of rectangle:"))
r=Rectangle(l,b)
r.area()
s=int(input("Enter the side of rectangle:"))
a=Square(s)
a.area()



