def my_decorator(func):
    def wrapper():
        print("1. something is happening before function is called.")
        func() #Executes the original function
        print("2. something is happening after function is called.")
    return wrapper

def say_hello():
    print(" Hello!")
    
# Decorating the function manually
say_hello = my_decorator(say_hello)
# calling the decorator function
say_hello()

