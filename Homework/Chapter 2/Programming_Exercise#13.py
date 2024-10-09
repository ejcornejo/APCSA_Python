def main():
    row_length = int(input("Enter the length of the row, in feet: "))
    endpost_space = int(input("Enter the the amount of space, in feet, used by an end-post assembly: "))
    vine_space = int(input("Enter the space between vines, in feet: "))
    
    grapevine_num = (row_length - (2 * endpost_space)) / vine_space
    
    print("You will be able to have", grapevine_num, "grapevines that wil fit in each row")

main()