def proptax():
    
    actual_value = int(input("Please enter the actual value of your property: "))
    
    assesment_value = actual_value * 0.60
    
    tax = assesment_value / 100
        
    property_tax = tax * 0.72
    
    print()
    print("The assessment value of your property is: $", assesment_value, "dollars.")
    print("The tax for the property will be,", format(property_tax,".2f"), "dollars.")
    
    
    
proptax()