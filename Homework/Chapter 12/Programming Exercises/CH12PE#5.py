def main():
    lst = []
    num_elements = int(input("Please enter how many elements you would like in the list: "))
    print()
    
    result = 0
    
    for i in range(num_elements):
        value = int(input(f"Enter element {i+1}: "))
        
        lst.append(value)
        
        result += sum(lst)
        
    print()
    print("The sum of the elements in your list are:", result)
    
def sum(list):
    
    sums = 0
    
    if len(list) == 1:
        return list[0]
    
    else:
        sums += sum(list[1:])
        
    return sums
        
main()