def time_calc():
    print("Hey! You're here to calculate time. I want to make sure that you are aware that")
    print("this program assumes multiples of the time units, so answers may not be gramitically correct.")
    print()
    seconds = int(input("Anyway... Let's begin! Please enter any number of seconds: "))
    
    if seconds < 60:
        
        print("there are", seconds, "seconds for your time.")
    
    else:
        if seconds >= 60 and seconds <= 3599:
            
            minutes = seconds // 60
            
            ts = seconds % 60
            
            print("there are", minutes, "minutes, and", ts, "seconds for your time.")
            
        elif seconds >= 3600 and seconds <= 86399:
            
            hours = seconds // 3600
            
            minutes = (seconds % 3600) // 60
            
            ts = seconds % 60
            
            print("there are", hours, "hours,", minutes, "minutes, and", ts, "seconds for your time.")
            
        elif seconds >= 86400:
            
            days = seconds // 86400
            
            hours = (seconds % 86400) // 3600
            
            minutes = (seconds % 3600) // 60
            
            ts = seconds % 60
            
            print("there are", days, "days", hours, "hours,", minutes, "minutes, and", ts, "seconds for your time.")
    
time_calc()