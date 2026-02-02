weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))

bmi = weight / (height * height)

print("Your BMI is:", bmi)

if bmi < 18.5:
    print("Category: Underweight")

elif bmi >= 18.5 and bmi < 25:
    print("Category: Normal weight")

elif bmi >= 25 a
