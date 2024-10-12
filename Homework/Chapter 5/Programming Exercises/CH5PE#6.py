def calories():
    
    fat_grams = int(input("Please enter the number of grams of fat you ate today: "))
    
    fat_calories = fat_grams * 9
    
    print()
    print("You are getting", fat_calories, "calories from the grams of fat you ate today.")
    print()
    
    carb_grams = int(input("Please enter the number of grams of carbs you ate today: "))
    
    carb_calories = carb_grams * 4
    
    print()
    print("You are getting,", carb_calories, "calories from the grams of carbs you ate today.")
    
    
calories()