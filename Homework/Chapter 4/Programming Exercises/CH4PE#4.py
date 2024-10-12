def distance():
    speed = int(input("What is the speed of the vehicle in mph? "))
    time = int(input("How many hours has it traveled? "))
    hours = 0
    
    print()
    print("  Hour		  Distance Traveled")
    print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
    
    while hours < time:
        hours += 1
        
        print("  ",hours, "			", (speed * hours))
    
       
distance()