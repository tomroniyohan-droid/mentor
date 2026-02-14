def input_units():
    units = int(input("Enter units consumed: "))
    return units

def calculate_bill(units):
    bill = 0
    if units <= 100:
        bill = units * 2
    elif units <= 300:
        bill = (100 * 2) + (units - 100) * 3
    else:
        bill = (100 * 2) + (200 * 3) + (units - 300) * 5
    return bill

def generate_bill_summary(units, bill):
    print("\nElectricity Bill Summary")
    print("Units Consumed:", units)
    print("Total Bill Amount: ₹", bill)

units = input_units()
bill_amount = calculate_bill(units)
generate_bill_summary(units, bill_amount)
