#variable in python
# variable is a container to store data value
#no command to declare a variable, just assign a value to a variable to form a variable.
# variable does not need to declare its type, python interpreter infers the type based on the value assigned to the variable.
#you can change the value of a variable at any time, and the type will be updated accordingly.
#example:
x = 5 #integer variable
y = "Hello, Python!" #string variable
print(x)
print(y)    
#reassigning variable
x = "Now I'm a string"
print(x)
#variable names must start with a letter or underscore, followed by letters, digits, or underscores.
#variable names are case-sensitive.
#example of invalid variable names:
#1name = 10 (starts with a digit)
#my-variable = 20 (contains a hyphen)
#Valid variable names:
name1 = "Alice"
_my_variable = 30
print(name1)
print(_my_variable)
#CASES FOR VARIABLE NAMING:
#1. camelCase
myVariableName = "Camel Case"# first word lowercase, subsequent words capitalized
print(myVariableName)
#2. snake_case
my_variable_name = "Snake Case"# all words lowercase, separated by underscores
print(my_variable_name)
#3. PascalCase
MyVariableName = "Pascal Case"# all words capitalized, no separators    
print(MyVariableName)

