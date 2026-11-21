"""Python control flow and loops: executable examples."""


# Conditional statements
age = 20
if age >= 18:
    print("You are eligible to vote")

age = 16
if age >= 18:
    print("Adult")
else:
    print("Minor")

marks = 85
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")

age = 22
has_id = True
if age >= 18:
    if has_id:
        print("You can enter")
    else:
        print("ID required")
else:
    print("You are underage")

# Pattern matching (Python 3.10+)
day = 2
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Invalid day")

# Short-circuit evaluation
age = 15
if age >= 18 and age <= 60:
    print("Eligible")
else:
    print("Not eligible")

age = 20
if age >= 18 or age == 15:
    print("Allowed")

# Ternary operator
age = 20
result = "Adult" if age >= 18 else "Minor"
print(result)


# for loop
for i in range(5):
    print(i)

# while loop
i = 1
while i <= 5:
    print(i)
    i += 1

# range forms
for i in range(5):
    print(i)

for i in range(2, 7):
    print(i)

for i in range(2, 11, 2):
    print(i)

# break
for i in range(1, 10):
    if i == 5:
        break
    print(i)

# continue
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

# pass
for i in range(5):
    if i == 3:
        pass
    print(i)

# Nested loops
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)
