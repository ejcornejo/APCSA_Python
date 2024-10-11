def roman_numerals():
    num = int(input('Please enter a number between 1 and 10: '))
    
    if num == 1:
        print(num, 'is "I" in roman numeral form')
    elif num == 2:
        print(num, 'is "II" in roman numeral form')
    elif num == 3:
        print(num, 'is "III" in roman numeral form')
    elif num == 4:
        print(num, 'is "IV" in roman numeral form')
    elif num == 5:
        print(num, 'is "V" in roman numeral form')
    elif num == 6:
        print(num, 'is "VI" in roman numeral form')
    elif num == 7:
        print(num, 'is "VII" in roman numeral form')
    elif num == 8:
        print(num, 'is "VIII" in roman numeral form')
    elif num == 9:
        print(num, 'is "IX" in roman numeral form')
    elif num == 10:
        print(num, 'is "X" in roman numeral form')
    else:
        print('**ERROR** Uh oh, you messed up. You need to put a number 1-10')
    

        
roman_numerals()