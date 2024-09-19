def main():
    
    #Ask the user to input feet and inches
    
    feetinput = int(input("Please enter the number of feet you would like to convert: "))
    inchesinput = int(input("Please enter the number of inches you would like to convert: "))
    
    #Convert feet and inches to total inches
    total = feetinput * 12 + inchesinput
    
    #Convert total inches to other units
    feet = total / 12
    yards = feet / 3
    miles = feet / 5280
    meters = feet * 0.3048
    centimeters = meters * 100
    millimeters = centimeters * 10
    kilometers = meters / 1000

    #Print the conversions
    print()
    print("Conversions:")
    print("Inches:", total)
    print("Feet:", feet)
    print("Yards:", yards)
    print("Miles:", miles)
    print("Meters:", meters)
    print("Centimeters:", centimeters)
    print("Millimeters:", millimeters)
    print("Kilometers:", kilometers)

main()