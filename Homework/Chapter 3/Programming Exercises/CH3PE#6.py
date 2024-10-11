def magic_dates():
    month = int(input("Please enter a month (January = 1, February = 2, March = 3...): "))
    print()
    date = int(input("Please enter a day in that month: "))
    print()
    year = int(input("Finally, please enter the last two digits of any year (i.e, 2000 = 00): "))
    print()
    
    if month * date == year:
        print("Wowzers!!!", month, "/",date, "/", year, "is MAGIC!")
        
    else:
        print("Your date of" , month, "/",date, "/", year, "is not magical")
        print('**hint: to be a "magic" date, the month * the date = the year**')
        
magic_dates()