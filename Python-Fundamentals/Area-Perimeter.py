"""Program to create a class Rectangle with data members length and width and a method 
which will compute the area and perimeter of rectangle. Inherit a class Box that contains 
additional method volume. Override the perimeter method to compute perimeter of a Box. 
Display details Rectangle and Box."""
class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width
    def perimeter(self):
        return 2*(self.length+self.width)
    def display(self):
        print("------Rectangle Details------")
        print("Length:",self.length)
        print("Width:",self.width)
        print("Area:",self.area())
        print("Perimeter:",self.perimeter())

class box(Rectangle):
    def __init__(self,length,width,height):
        super().__init__(length,width)
        self.height=height
    def volume(self):
        return self.length*self.width*self.height
    def perimeter(self):
        return 4*(self.length+self.width+self.height)
    def display(self):
        print("\n------Box Details------")
        print("Length:",self.length)
        print("Width:",self.width)
        print("Height:",self.height)
        print("Area of Base:",self.area())
        print("Perimeter of Box:",self.perimeter())
        print("Volume:",self.volume())

length,width=map(float,input("Enter length and width:").split())
r=Rectangle(length,width)
r.display()
height=float(input("\nEnter height:"))
b=box(length,width,height)
b.display()
             
