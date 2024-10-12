def penny_pay():
    print("I heard your salary is one penny the first day, two pennies the second day, and continues to double each day")
    print()
    penny = 0.01
    day = int(input("Please enter the number of days you've been on the job: "))
    count = 0
    total = 0
    
    print()
    print(" Day					 Money Earned")
    print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
    print()
    
    while count < day:
        
        count += 1
        
        print(" ",count, "					    $", penny)
        
        total = penny + total
        
        penny = penny * 2
        
        
    print("---------------------------------------------------------")
    print()
    print("Your total money that you gained from your salary over", day,"days is $", total)
    print()

    
penny_pay()