try:
    number = int(input("Enter a number: "))
    result = 10 / number
except ZeroDivisionError:
    print("Error: You cannot divide by zero!")
except ValueError:
    print("Error: Please enter a valid integer.")
else:
    print(f"Success! The result is {result}")
finally:
    print("This block always runs, no matter what.")
