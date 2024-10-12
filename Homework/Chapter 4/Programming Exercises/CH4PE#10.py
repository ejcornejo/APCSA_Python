def tuition_inflation():
    tuition = 8000
    
    for i in range(1, 6):
        print("Year", i,": The tuituon will be: $", tuition)
        
        tuition += (tuition * 0.03)
         
    
tuition_inflation()