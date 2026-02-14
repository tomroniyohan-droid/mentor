def calculator():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")
    choice = int(input("Select operation: "))

    if choice == 1:
        print("Result:", a + b)
    elif choice == 2:
        print("Result:", a - b)
    elif choice == 3:
        print("Result:", a * b)
    elif choice == 4:
        if b != 0:
            print("Result:", a / b)
        else:
            print("Division by zero not allowed")
    else:
        print("Invalid operation")

def string_operations():
    s = input("Enter a string: ")

    print("\n1. Convert to Uppercase")
    print("2. Convert to Lowercase")
    print("3. Reverse String")
    print("4. Find Length")

    choice = int(input("Select operation: "))

    if choice == 1:
        print("Result:", s.upper())
    elif choice == 2:
        print("Result:", s.lower())
    elif choice == 3:
        print("Result:", s[::-1])
    elif choice == 4:
        print("Length:", len(s))
    else:
        print("Invalid choice")

def number_utilities():
    n = int(input("Enter a number: "))

    print("\n1. Check Even or Odd")
    print("2. Check Prime")
    print("3. Find Factorial")

    choice = int(input("Select operation: "))

    if choice == 1:
        if n % 2 == 0:
            print("Even Number")
        else:
            print("Odd Number")
    elif choice == 2:
        if n > 1:
            for i in range(2, n):
                if n % i == 0:
                    print("Not a Prime Number")
                    break
            else:
                print("Prime Number")
        else:
            print("Not a Prime Number")
    elif choice == 3:
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        print("Factorial:", fact)
    else:
        print("Invalid choice")

while True:
    print("\n--- Menu-Driven Utility Application ---")
    print("1. Calculator")
    print("2. String Operations")
    print("3. Number Utilities")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        calculator()
    elif choice == 2:
        string_operations()
    elif choice == 3:
        number_utilities()
    elif choice == 4:
        print("Exiting application...")
        break
    else:
        print("Invalid choice! Try again.")
