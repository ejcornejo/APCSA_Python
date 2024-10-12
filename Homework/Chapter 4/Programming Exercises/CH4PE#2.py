def calories():
    print("To calculate the calories you burned after 10, 15, 20, 25, and 30 minutes.")
    print()
    cal_burned = 4.2
    
    for i in range(10, 31):
        if i % 5 == 0:
            
            print("After", i, "minutes, you burned", (i * 4.2), "calories.")
            
            
calories()