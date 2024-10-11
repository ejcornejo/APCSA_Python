def grade_calc():
    test_1 = int(input("Please enter tne grade of your first test, (no more than 25 points): "))
    test_2 = int(input("Please enter tne grade of your second test, (no more than 25 points): "))
    exam = int(input("Please enter tne grade you got on your main exam, (no more than 50 points): "))
    
    total = test_1 + test_2 + exam #calculating a total score
    
    if test_1 < 0 or test_2 < 0 or exam < 0 or test_1 > 25 or test_2 > 25 or exam > 50: #in case user inputs invalid score
        print("**Error**, you did not put in an accepted score.")
        print()
        print()
        print("                             Try again later.")
        
    else:
        if total >= 80: #depending on what "total" is gives grade
            print('You get a "Distinction" grade')
        elif total < 50 or exam < 25:
            print('You get a "Fail" grade')
        elif total <=59 and total >= 50:
            print('You get a "Pass" grade')
        elif total < 80 and total >= 60:
            print('You get a "Credit" grade')

grade_calc()       