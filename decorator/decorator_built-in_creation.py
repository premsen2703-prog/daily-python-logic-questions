def my_decorator(func):
    def wrapper():
        print("1. something is happening before function is called.")
        func() #Executes the original function
        print("2. something is happening after function is called.")
    return wrapper

@my_decorator
def say_hello():
    print(" Hello!")

say_hello() #gives the exact output as above!