employees = {}

def add_employee(emp_id, name, basic_salary):
    employees[emp_id] = {
        "Name": name,
        "Basic": basic_salary,
        "Bonus": 0,
        "Deduction": 0
    }
    print("Employee added:", name)

def calculate_salary(basic, bonus=0, deduction=0):
    return basic + bonus - deduction

def update_bonus_deduction(emp_id, bonus=0, deduction=0):
    if emp_id in employees:
        employees[emp_id]["Bonus"] = bonus
        employees[emp_id]["Deduction"] = deduction
    else:
        print("Employee not found")

def generate_payroll_report():
    print("\nPayroll Report")
    print("-" * 40)
    for emp_id, data in employees.items():
        net_salary = calculate_salary(
            data["Basic"],
            data["Bonus"],
            data["Deduction"]
        )
        print("Employee ID:", emp_id)
        print("Name:", data["Name"])
        print("Basic Salary:", data["Basic"])
        print("Bonus:", data["Bonus"])
        print("Deduction:", data["Deduction"])
        print("Net Salary:", net_salary)
        print("-" * 40)

add_employee(101, "Adarsh", 30000)
add_employee(102, "Rahul", 28000)

update_bonus_deduction(101, bonus=5000)
update_bonus_deduction(102, bonus=3000, deduction=1000)

generate_payroll_report()


