# Project 02

op = input("Enter the type of operation(+, -, *, /): ")
a = float(input("Enter the 1st number: "))
b = float(input("Enter the 2nd number: "))

if op == '+':
    result = a + b
    print(f"Result: {result}")
elif op == '-':
    result = a - b
    print(f"Result: {result}")
elif op == '*':
    result = a * b
    print(f"Result: {result}")
elif op == '/':
    result = a / b
    print(f"Result: {result}")
else:
    print("The operation you entered is either invalid or not available")