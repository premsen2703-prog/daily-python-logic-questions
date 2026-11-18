# def my_function():
#     return "Hello prem!"

# print(my_function())

def func_takes_arg_as_tuple(*name):# it takes argument as a tuple 
    print(f"your name is: {name[1]}")

func_takes_arg_as_tuple("prem sen","priyanka sen")
func_takes_arg_as_tuple("rajesh sen","preeti sen")

def func_takes_arg_as_dictionary(**name):# it takes argument as a dictionary
    print(f"your name is: {name['person1']}")

func_takes_arg_as_dictionary(person1 = "prem sen", person2 = "priyanka sen")
func_takes_arg_as_dictionary(person1 = "rajesh sen", person2 ="preeti sen")

def func_takes_only_positional_arg(x,/):# using ,/ after argument's name for only passing positional arguments in function
    print(x*5)
func_takes_only_positional_arg(5)

def func_takes_only_keywords_arg(*,x):# using *, before argument's name for only passing keyword argument in function
    print(x*5)

func_takes_only_keywords_arg(x = 5)

def func_takes_both_positional_and_keywords_arg(a,b,/,*,c,d):# using both ,/(after arguments) and ,*(before arguments) 
    print(a+b+c+d)

func_takes_both_positional_and_keywords_arg(2,3,c = 3,d = 2)

# def recursion(): # this is recursion which which means function calls itself 
#     print("this is recursion function")
#     recursion()
# recursion()

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
n = int(input("ENTER N: "))
print(f"factorial of {n} is {factorial(n)}")



