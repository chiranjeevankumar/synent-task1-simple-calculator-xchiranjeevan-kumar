
def calculator():
    print("=== Simple Calculator ===")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    choice = input("Choose an operation (1-4): ").strip()

    if choice not in {"1", "2", "3", "4"}:
        print("Invalid operation. Choose 1, 2, 3, or 4.")
        return

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter valid numbers only.")
        return

    if choice == "1":
        result = num1 + num2
    elif choice == "2":
        result = num1 - num2
    elif choice == "3":
        result = num1 * num2
    else:
        if num2 == 0:
            print("Error: Cannot divide by zero.")
            return
        result = num1 / num2

    print("Result:", result)


if __name__ == "__main__":
    calculator()
