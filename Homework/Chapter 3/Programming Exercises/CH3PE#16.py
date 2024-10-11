def feb_days():
   
    year = int(input("Type in any year in a 4 digit format, like 2020: "))
        
    if year > 9999:
        print("You inputed a year that is not in a 4 digit formart, please try again.")
        print()
        return feb_days()
    
    elif year < 1000:
        print("You inputed a year that is not in a 4 digit formart, please try again.")
        print()
        return feb_days()
    
    elif (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print ("For February", year, "it has the mythical and magical 29 DAYS!")
            
    else:
        print ("For February", year, "it has 28 days...")
            
feb_days()