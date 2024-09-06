import math

def main():
    radius = float(input("Enter the radius of a circle:"))
    if (radius >= 0):
        area = math.pi * radius **2
        print('A circle with a radius of ', radius,'has an area of ', area)
    else:
            print('Negative radius entered: ', radius)
            
main()