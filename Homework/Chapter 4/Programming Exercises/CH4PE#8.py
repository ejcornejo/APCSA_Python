def avg_length():
     print("A fun little program to show the average amount of letters of words you enter!")
     print("*Please enter at least 2 words for the program to work a little more properly*")
     print()
     count = 1
     num = -1
     letters = 0
     while count != 0:
         
         num += 1 
         
         word = input("Please enter any word you'd like or press 'Enter'/'return' (with nothing) to stop: ")
         print()
         
         letters = letters + len(word)
        
         
         if word == "":
             
             count = 0
             
             print()
             print("You have typed", num, "words.")
             print("The average length of all your words is", (letters//num), "letters!")
avg_length()