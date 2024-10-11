def hotdog_calc():
    print("I hear you're having a Hot Dog Cookout! I am here to help you.")
    people = int(input("Please tell me the amount of people that are going: "))
    hotdogs = int(input("And tell me how many hot dogs each person gets: "))
    
    needed = people * hotdogs
    
    buns = 8
    pack = 10
    
    packnum = needed // pack
    bunnum = needed // buns
    leftoverHD = pack - (needed % pack)
    leftoverBUNS = buns - (needed % buns)
    
    print()
    print()
    print("The minimum number of hot dog packs you need is", packnum)
    print("The minimum number of hot dog bun packs you need is", bunnum)
    print("The number of hot dogs you will have leftover is", leftoverHD)
    print("The number of hot dog buns you will have leftover is", leftoverBUNS)
    print()
    print("Hope this helped! :)")
    
hotdog_calc()