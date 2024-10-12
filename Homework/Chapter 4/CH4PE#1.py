def bugs():
    print("Hello there Bug Collecter!")
    print()
    total = 0

    for day in range (1,6):
        
        bugs_collected = int(input(f"Please enter the number of bugs collected on day {day}: "))
        total += bugs_collected
     
    print()
    print(f"The total number of bugs you collected over the 5 days is: {total}")

bugs()
