age = int(input("Enter your age: "))
gender = input("Enter your gender (M/F): ")

if gender == 'M' or gender == 'm':
    if 20 <= age <= 60:
        print("Eligible for Insurance (Male)")
    else:
        print("Not Eligible for Insurance (Male)")

elif gender == 'F' or gender == 'f':
    if 18 <= age <= 55:
        print("Eligible for Insurance (Female)")
    else:
        print("Not Eligible for Insurance (Female)")

else:
    print("Invalid gender input")