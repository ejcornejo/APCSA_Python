import math

def circle():
    r = int(input("please input the radius of your circle "))
    C = 2 * math.pi * r
    A = math.pi * r ** 2
    
    print("The area of your circle is", A)
    print("The circumference of your circle is", C)
    
circle()
