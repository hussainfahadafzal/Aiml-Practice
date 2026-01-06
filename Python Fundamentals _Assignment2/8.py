def calculator(a, b, operation):
    match operation:
        case '+':
            return a + b
        case '-':
            return a - b
        case '*':
            return a * b
        case '/':
            if b == 0:
                return "Division by zero not allowed"
            return a / b
        case _:
            return "Invalid operation"

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
op = input("Enter operation (+, -, *, /): ")

print("Result:", calculator(a, b, op))
