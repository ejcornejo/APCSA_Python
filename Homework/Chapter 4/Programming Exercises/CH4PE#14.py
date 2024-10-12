def main():
    rows = int(input("How many rows do you want to have? "))
    print()
    
    for i in range(1, rows+1):
        print("*" * rows)
        
        rows -= 1
    

main() #To draw that specific pattern, enter 7.