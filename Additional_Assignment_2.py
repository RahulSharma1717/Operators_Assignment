# Take two variables and divide one with another in such a way that the quotient comes as output.

# Answer:
# Input two numbers
num1 = float(input("Enter the numerator: "))
num2 = float(input("Enter the denominator: "))

# Perform the division and display the quotient
if num2 != 0:  # Ensure the denominator is not zero
    quotient = int(num1 // num2)
    print(f"The quotient is: {quotient}")
else:
    print("Error: Division by zero is not allowed.")
