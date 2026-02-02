usd_rate = 83.0     
eur_rate = 90.0

print("Currency Converter")
print("1. INR to USD")
print("2. USD to INR")
print("3. INR to EUR")
print("4. EUR to INR")

choice = int(input("Enter your choice (1-4): "))

amount = float(input("Enter the amount: "))

if choice == 1:
    result = amount / usd_rate
    print("INR", amount, "=", result, "USD")

elif choice == 2:
    result = amount * usd_rate
    print("USD", amount, "=", result, "INR")

elif choice == 3:
    result = amount / eur_rate
    print("INR", amount, "=", result, "EUR")

elif choice == 4:
    result = amount * eur_rate
    print("EUR", amount, "=", result, "INR")

else:
    print("Invalid choice")
