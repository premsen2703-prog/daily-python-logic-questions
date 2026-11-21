# f-Strings
# Very important
# An f-string is a modern and easy way to insert variables and expressions directly inside a string.

# It was introduced in Python 3.6.
# Syntax
f"Your text {variable}" # type: ignore



# Notice the f before the quotation marks.
# Example 1: Basic f-string
name = "Prem"
age = 21
print(f"My name is {name} and my age is {age}")



# Output:
# My name is Prem and my age is 21


# Example 2: Performing calculations
# You can perform calculations inside curly braces.
a = 10
b = 20
print(f"Sum = {a + b}")
print(f"Multiplication = {a * b}")



# Output:
# Sum = 30
# Multiplication = 200


# Example 3: Formatting decimal numbers
price = 123.45678
print(f"Price: {price:.2f}")



# Output:
# Price: 123.46


# Here, .2f means display two digits after the decimal point.
# Example 4: Adding commas to numbers
salary = 500000
print(f"Salary: {salary:,}")



# Output:
# Salary: 500,000


# Example 5: Percentage formatting
percentage = 0.8567
print(f"Percentage: {percentage:.2%}")



# Output:
# Percentage: 85.67%


# Difference between .format() and f-strings
# Feature	.format()	f-string
# Syntax	.format()	f""
# Readability	Good	Very good
# Calculations inside string	Less convenient	Easy
# Modern usage	Yes	Preferred
# Example	"{}".format(name)	f"{name}"

