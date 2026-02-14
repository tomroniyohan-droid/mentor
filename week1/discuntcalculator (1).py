amount = float(input("Enter total purchase amount: "))
discount = 0

if amount >= 5000:
    discount = amount * 0.20   

elif amount >= 3000:
    discount = amount * 0.15   

elif amount >= 1000:
    discount = amount * 0.10   

else:
    discount = 0               

final_amount = amount - discount

print("Discount Amount: $", discount)
print("Amount to Pay: $", final_amount)
