def sales_report():
    print("\n--- Sales Report ---")
    print("Total Sales: ₹50,000")
    print("Total Orders: 120")

def inventory_report():
    print("\n--- Inventory Report ---")
    print("Available Items: 350")
    print("Out of Stock Items: 20")

def employee_report():
    print("\n--- Employee Report ---")
    print("Total Employees: 45")
    print("Active Employees: 42")

def generate_report(report_function):
    report_function()

print("Select Report Type:")
print("1. Sales Report")
print("2. Inventory Report")
print("3. Employee Report")

choice = int(input("Enter your choice: "))

if choice == 1:
    generate_report(sales_report)
elif choice == 2:
    generate_report(inventory_report)
elif choice == 3:
    generate_report(employee_report)
else:
    print("Invalid choice")
