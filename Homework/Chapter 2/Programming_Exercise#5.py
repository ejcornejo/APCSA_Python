#File: Programming_Exercise#5
#Student: Esteban Cornejo
#
#Date: October 8, 2024
#Description of Program: This program shows the distance that a car
# travels down the interstate after a certain amount of hours
#GitHub: ejcornejo

def distance_traveled():
    speed = 70
    time_6 = 6
    time_10 = 10
    time_15 = 15
    
    distance_6 = speed * time_6
    distance_10 = speed * time_10
    distance_15 = speed * time_15
    
    print(f"The distance traveled in 6 hours is {distance_6} miles.")
    print(f"The distance traveled in 10 hours is {distance_10} miles.")
    print(f"The distance traveled in 15 hours is {distance_15} miles.")

distance_traveled()