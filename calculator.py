def calculate():
    number1 = float(input("Enter first number: "))
    number2 = float(input("Enter second number: "))
    operator = input("Enter operator (+, -, *): ")

    operations = {
        "+": number1 + number2,
        "-": number1 - number2,
        "*": number1 * number2
    }

    result = operations.get(operator, "Not a valid operator...")
    print("Result:", result)

calculate()