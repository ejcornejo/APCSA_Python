#File: Programming_Exercise#9
#Student: Esteban Cornejo
#
#Date: October 8, 2024
#Description of Program: The program asks the user to enter the radius
# of a circle. The program should calculate and display the area
# and circumference of the circle  
#GitHub: ejcornejo

import math

def circle():
    r = int(input("please input the radius of your circle "))
    C = 2 * math.pi * r
    A = math.pi * r ** 2
    
    print("The area of your circle is", A)
    print("The circumference of your circle is", C)
    
circle()