def restraunt():
    vegeterian = input("Is anyone in your party vegetarian? ")
    vegan = input("Is anyone in your party vegan? ")
    gluten_free = input("Is anyone in your party gluten-free? ")

    if vegeterian == "yes":
        
        if vegan == "yes":
            
            if gluten_free == "yes":
                print("Well then, you are able to go to:")
                print("- Corner Cafe")
                print("- The Chef's Kitchen")
            
            elif gluten_free == "no":
                print("Well then, you are able to go to:")
                print("- Corner Cafe")
                print("- The Chef's Kitchen")
        
        elif vegan == "no":
            
            if gluten_free == "yes":
                print("Well then, you are able to go to:")
                print("- Corner Cafe")
                print("- Main Street Pizza Company")
                print("- The Chef's Kitchen")
            
            elif gluten_free =="no":
                
                print("Well then, you are able to go to:")
                print("- Corner Cafe")
                print("- Main Street Pizza Company")
                print("- The Chef's Kitchen")
                print("- Mama's Fine Italian")
                
    elif vegeterian == "no":
        if vegan == "yes":
            
            if gluten_free == "yes":
                print("Well then, you are able to go to:")
                print("- Corner Cafe")
                print("- The Chef's Kitchen")
            
            elif gluten_free =="no":
                print("Well then, you are able to go to:")
                print("- Corner Cafe")
                print("- The Chef's Kitchen")
        
        elif vegan == "no":
            
            if gluten_free == "yes":
                print("Well then, you are able to go to:")
                print("- Corner Cafe")
                print("- Main Street Pizza Company")
                print("- The Chef's Kitchen")
            
            elif gluten_free =="no":
                print("Well then, you are able to go to:")
                print("-Joe's Gourmet Burgers")
                print("- Corner Cafe")
                print("- Main Street Pizza Company")
                print("- The Chef's Kitchen")
                print("- Mama's Fine Italian")
    else:
        print("Make sure to have no Capitals in your response! That is considered an invalid response!")
                
    
                
restraunt()