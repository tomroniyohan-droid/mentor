# Function to input employee details
def input_employee_details():
    emp_id = input("Enter Employee ID: ")
    emp_name = input("Enter Employee Name: ")
    basic_salary = float(input("Enter Basic Salary: "))
    return emp_id, emp_name, basic_salary


# Function to calculate gross salary
def calculate_gross_salary(basic_salary):
    hra = basic_salary * 0.20      # 20% HRA
    da = basic_salary * 0.10       # 10% DA
    gross_salary = basic_salary + hra + da
    return gross_salary


# Function to calculate deductions
def calculate_deductions(gross_salary):
    pf = gross_salary * 0.12       # 12% PF
    tax = gross_salary * 0.10      # 10% Tax
    total_deductions = pf + tax
    return total_deductions


# Function to display final salary
def display_salary(emp_id, emp_name, gross_salary, deductions, net_salary):
    print("\n--- Employee Salary Details ---")
    print("Employee ID   :", emp_id)
    print("Employee Name :", emp_name)
    print("Gross Salary  :", gross_salary)
    print("Deductions    :", deductions)
    print("Net Salary    :", net_salary)


# Main Program
emp_id, emp_name, basic_salary = input_employee_details()

gross_salary = calculate_gross_salary(basic_salary)
deductions = calculate_deductions(gross_salary)
net_salary = gross_salary - deductions

display_salary(emp_id, emp_name, gross_salary, deductions, net_salary)
