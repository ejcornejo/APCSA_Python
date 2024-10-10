def compare_amounts():
    amount1 = int(input("Please enter the 1st number: "))
    amount2 = int(input("Please enter the 2nd number: "))
    
    if amount1 > 10 and amount2 < 100:
        if amount1 > amount2:
            print("It seems that", amount1, "is greater than", amount2)
        else:
            print("It seems that", amount2, "is greater than", amount1)
    else:
        print()
        print("Please try again!")
        print("Make sure the 1st number is greater than 10.")
        print("Also, make sure the 2nd number is less than 100.")
        
compare_amounts()
