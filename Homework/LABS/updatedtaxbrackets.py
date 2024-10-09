def compute_tax_single(income):
    if income <= 11_600: 
        tax = income * 0.1
        bracket = '10% tax bracket'
    elif income <= 47_150:
        tax = 1_160 + (income - 11_600) * 0.12
        bracket = '12% tax bracket'
    elif income <= 100_525:
        tax = 1_160 + 4_260 + (income - 47_150) * 0.22
        bracket = '22% tax bracket'
    elif income <= 191_950:
        tax = 1_160 + 4_260 + 11_748.3 + (income - 100_525) * 0.24
        bracket = '24% tax bracket'
    elif income <= 243_725:
        tax = 1_160 + 4_260 + 11_748.3 + 21_506 + (income - 191_950) * 0.32
        bracket = '32% tax bracket'
    elif income <= 609_350:
        tax = 1_160 + 4_260 + 11_748.3 + 21_506 + 16_560 + (income - 243_725) * 0.35
        bracket = '35% tax bracket'
    else:
        tax = 1_160 + 4_260 + 11_748.3 + 21_506 + 16_560 + 127_709.5 + (income - 609_350) * 0.37
        bracket = '37% tax bracket'
    return tax, bracket


def compute_tax_married(income):
    if income <= 23_200:
        tax = income * 0.1
        bracket = '10% tax bracket'
    elif income <= 94_300:
        tax = 2_320 + (income - 23_200) * 0.12
        bracket = '12% tax bracket'
    elif income <= 201_050:
        tax = 2_320 + 8_532 + (income - 94_300) * 0.22
        bracket = '22% tax bracket'
    elif income <= 383_900:
        tax = 2_320 + 8_532 + 23_487 + (income - 201_050) * 0.24
        bracket = '24% tax bracket'
    elif income <= 487_450:
        tax = 2_320 + 8_532 + 23_487 + 43_788 + (income - 383_900) * 0.32
        bracket = '32% tax bracket'
    elif income <= 731_200:
        tax = 2_320 + 8_532 + 23_487 + 43_788 + 33_130 + (income - 487_450) * 0.35
        bracket = '35% tax bracket'
    else:
        tax = 2_320 + 8_532 + 23_487 + 43_788 + 33_130 + 170_812.5 + (income - 731_200) * 0.37
        bracket = '37% tax bracket'
    return tax, bracket


def get_marital_status():
    # Asks the user for a valid input
    ## It will keep asking until the user provides a valid input
    while True:
        marital_status = input("Enter your marital status (s or m): ").lower().strip()
        if marital_status in ["s", "m"]:
            return marital_status
        else:
            print("There is no 'it's complicated', enter 's' or 'm'!")


def main():
    print("Welcome to our friendly tax computing program.")
    print("Please follow the directions.\n")
    
    # Get marital status with validation
    marital_status = get_marital_status()
    
    # Get taxable income
    try:
        income = float(input("Enter your taxable income: "))
        if income < 0:
            print("\nNegative income reported! Try again later.")
            return
    except ValueError:
        print("\nInvalid income entered! Try again later.")
        return

    # Compute taxes based on marital status
    if marital_status == "s":
        tax, bracket = compute_tax_single(income)
        status = "Single"
    else:
        tax, bracket = compute_tax_married(income)
        status = "Married"
    
    # Print the results
    print(f"\nMarital status: {status}")
    print(f"Taxable income: ${income:,.2f}")
    print(f"Taxes owed: ${tax:,.2f} ({bracket})")


main()
