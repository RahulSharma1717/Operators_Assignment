# Make a calculator like program where it perform additions, multiplication, division,subtraction on two values.

# Answer:
print("Welcome to the Calculator!")
print("It can perform basic Arithmetic Operations on 2 Numbers")

# Input two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Choose an operation:")
print("ADD - Addition")
print("SUB - Subtraction")
print("MUL - Multiplication")
print("DIV - Division")

# Input the operation abbreviation
operation = input("Enter your operation (ADD/SUB/MUL/DIV): ").strip().upper()

# Perform the operation based on the abbreviation
if operation == 'ADD':
    print(f"The result of addition is: {num1 + num2}")
elif operation == 'SUB':
    print(f"The result of subtraction is: {num1 - num2}")
elif operation == 'MUL':
    print(f"The result of multiplication is: {num1 * num2}")
elif operation == 'DIV':
    if num2 != 0:  # Avoid division by zero
        print(f"The result of division is: {num1 / num2}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation! Please select a valid option (ADD/SUB/MUL/DIV).")

