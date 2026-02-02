# Electricity Bill Calculator

units = int(input("Enter total units consumed: "))
bill = 0

if units <= 100:
    bill = units * 1.5

elif units <= 200:
    bill = (100 * 1.5)
    bill += (units - 100) * 2.5

elif units <= 300:
    bill = (100 * 1.5)
    bill += (100 * 2.5)
    bill += (units - 200) * 4

else:
    bill = (100 * 1.5)
    bill += (100 * 2.5)
    bill += (100 * 4)
    bill += (units - 300) * 5

print("Total Electricity Bill: $", bill)

