#program using user defined functions to find area of rectangle square circle and triangle.
#Function to find area of rectangle , square and triangle
def area_rectangle(length,breadth):
   return length*breadth
def area_square(side):
    return side*side
def area_circle(radius):
    pi=3.14
    return pi*r*r
def area_triangle(base,height):
    return 0.5*base*height

while True:
 print("-"*30)
 print("Area of calculation program")
 print("1.Rectangle")
 print("2.square")
 print("3.circle")
 print("4.Triangle")
 print("5.Exit")
 choice=int(input("Enter your choice(1-5):"))
    
 if choice==1:
    l=float(input("Enter Length:"))
    b=float(input("Enter Breadth:"))
    print("Area of the Rectangle is:",area_rectangle(l,b))
 elif choice==2:
    s=float(input("Enter side:"))
    print("Area of Square is:",area_square(s))
 elif choice==3:
    r=float(input("Enter the radius:"))
    print("Area of Circle is:",area_circle(r))
 elif choice==4:
    base=float(input("Enter the Base of the triangle:"))
    height=float(input("Enter height of the triangle:"))
 elif choice==5:
    print("Exiting Program...")
    break
 else:
    print("Invalid Choice!!!")
    
    
    
