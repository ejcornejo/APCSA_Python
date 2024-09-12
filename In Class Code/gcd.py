def gcd(a,b,):
    if a>b:
        small = b
        large = a
    else:
        small = a
        large = b
    r = large % small #remainder
    
    while r > 0:
        large = small
        small = r
        r = large%small
        print(large, small, r)#Order matters!!!
        
    return small

print(gcd(234,42))