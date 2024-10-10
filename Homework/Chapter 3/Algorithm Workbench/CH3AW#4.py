def grades():
    score = int(input("Enter your score: "))
    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60
    if score >= A_score:
        print('Your grade is an A.')
    elif score >= B_score:
        print('Your grade is a B.')
    elif score >= C_score:
        print('Your grade is a C.')
    elif score >= D_score:
        print('Your grade is a D.')
    else:
        print('Your grade is a F.')
        
grades()
