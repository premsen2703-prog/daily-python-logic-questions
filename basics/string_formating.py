#string formating means inserting a variable or value into a string in a readable way
#suppose you want to display a person's name or age 
name = "Prem"
age = 21
print("My name is ", name, "and my age is", age)
# o/p- My name is Prem and my age is 21

# Using string concatenation
print("My name is "+ name +" and my age is" + str(age))
#o/p- My name is Prem and my age is 21
#Notice that we used str(age) because we cannot directly concatenate a string and an integer.

# Using .format()
# Python provides the format() method to insert values into strings.
print("My Name is {} and my age is {}".format(name, age))
#o/p-My name is Prem and my age is 21

#You can also specify positions:
print("My name is {0} and my age is {1}".format(name, age))

#o/p- My name is Prem and my age is 21

# You can even change their order:
print("My age is {1} and my name is {0}".format(name, age))

# Output:
# My age is 21 and my name is Prem
