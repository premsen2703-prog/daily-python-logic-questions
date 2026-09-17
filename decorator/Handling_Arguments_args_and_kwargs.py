#Handling Arguments (*args and **kwargs)
#If the function you want to decorate takes parameters (like a user's name),
#  your internal wrapper function must be flexible enough to accept them. 
# We use *args and **kwargs for this.
def greeting_decorator(func):
    def wrapper(*args, **kwargs):
        print("Initializing greeting protocol...")
        result = func(*args, **kwargs)  # Captures any return value
        print("Protocol complete.")
        return result
    return wrapper

@greeting_decorator
def greet(name):
    print(f"Hi {name}!")

greet("Alice")
