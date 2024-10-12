def population():
    print("Hi, hope you are well!")
    pop = int(input("Please enter the number of organisms you're starting with: "))
    avg = float(input("Please enter the dailt average increase (as a percentage): "))
    days = int(input("Number of days that will pass: "))
    print()
    
    print("Day Approximate		 Population")
    print()
    
    for i in range (1, days + 1):
        
        print(i, "			", pop)
        
        pop += pop * (avg * 0.01)
        
population()