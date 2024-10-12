def main():
    lst = []
    num_elements = int(input("Please enter how many elements you would like in the list: "))
    print()
    
    for i in range(num_elements):
        value = int(input(f"Please enter element {i+1}: "))
        lst.append(value)
        
    largest_value = big(lst)
    print()
    print("The largest value in that list is:", largest_value)
    
def big(list):
    if len(list) == 1:
        return list[0]
        
    else:
        largest = big(list[1:])
        if list[0] > largest:
            return list[0]
        else:
            return largest
        
main()