def main():
    R = int(input("Enter the length of the row, in feet: "))
    E = int(input("Enter the the amount of space, in feet, used by an end-post assembly: "))
    S = int(input("Enter the space between vines, in feet: "))
    
    V = (R - (2 * E)) / S
    
    print("You will be able to have", V, "grapevines that wil fit in each row")

main()
