#input() funcvtion is used to take input from the user.
#  It takes input in the form of string. 
# If we want to take input in the form of integer or float,
# then we have to typecast it into int() or float() respectively.
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print("Hello,", name, "! You are", age, "years old.")
a = input("enter a first number")
b = input("enter a second number")
print(a + b)
# o/p - 1020 because python treats both as a stirng and join them together
#solution is type conversion
#  for integer
a = int(a)
b = int(b)
print(a + b)# here o/p will be 30
# for float
a = float(a)
b = float(b)
print(a+b)

# Important:
# Function	Purpose
# input()	Takes user input as a string
# int()	Converts into integer
# float()	Converts into decimal number
# str()	Converts into string

