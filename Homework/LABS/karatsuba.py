#File: initials.py
#Student: Esteban Cornejo
#
#Date: September 13, 2024
#Description of Program: This program is used to help a user with Karatsuba Multiplication
#GitHub: ejcornejo

n1 = int(input("Enter a 4-digit integer: "))  
n2 = int(input("Enter another 4-digit integer: "))  

a = n1 // 100  
b = n1 % 100   
c = n2 // 100  
d = n2 % 100   

print("n1:", n1, "split into", a, "and", b)
print("n2:", n2, "split into", c, "and", d)

step1 = a * c
print("Step 1 (a * c):", step1)

step2 = b * d
print("Step 2 (b * d):", step2)

step3 = (a + b) * (c + d)
print("Step 3 ((a + b) * (c + d)):", step3)

step4 = step3 - step1 - step2
print("Step 4 (Cross terms, step3 - step1 - step2):", step4)

ans = (step1 * 10000) + (step4 * 100) + step2
print("Final Result:", ans)
