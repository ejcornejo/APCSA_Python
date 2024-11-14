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
e = a * c
f = b * d
g = (a + b) * (c + d)
h = g - e - f
i = e * 10000
j = h * 100
k = i + j + f

real_answer = n1 * n2

print("________________________________________________________________________________________")
print("According to Karatsuba Multiplication, the answer is: ", k)
print()
print("The actual answer is", real_answer, "which is equal as computed before.")
