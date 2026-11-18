#problem statement: Write a program to check if a password is strong or not. A password is considered strong if it has at least 8 characters, contains at least one uppercase letter, at least one lowercase letter, and at least one digit.
#approach: We can use an if statement to check if the password meets the certain conditions
#code:
password="Abc12345"
if(len(password)>=8 and any(c.isupper() for c in password) and any(c.islower() for c in password) and any(c.isdigit() for c in password)):
    print("password is strong")
else:
    print("password is not strong")