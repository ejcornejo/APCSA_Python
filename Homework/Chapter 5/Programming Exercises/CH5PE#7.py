def seating_revenue():
    
    class_a = int(input("Please enter the number of Class A tickets sold: "))
    class_b = int(input("Please enter the number of Class B tickets sold: "))
    class_c = int(input("Please enter the number of Class C tickets sold: "))
    
    total = (class_a * 20) + (class_b * 15) + (class_c * 10)
    
    print()
    print("The income generated from the ticket sales is", total, "dollars.")
    
    
seating_revenue()