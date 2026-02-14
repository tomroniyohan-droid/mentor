def generate_bill(amount, tax_function):
    tax = tax_function(amount)
    total = amount + tax
    return tax, total

def tax_india(amount):
    return amount * 0.18   

def tax_usa(amount):
    return amount * 0.10   

def tax_uk(amount):
    return amount * 0.10

amount = float(input("Enter base amount: "))

print("\nSelect Region:")
print("1. India")
print("2. USA")
print("3. UK")

choice = int(input("Enter choice: "))

if choice == 1:
    tax, total = generate_bill(amount, tax_india)
elif choice == 2:
    tax, total = generate_bill(amount, tax_usa)
elif choice == 3:
    tax, total = generate_bill(amount, tax_uk)
else:
    print("Invalid choice")
    exit()

print("\n--- Bill Details ---")
print("Base Amount:", amount)
print("Tax Amount:", tax)
print("Total Amount:", total)
