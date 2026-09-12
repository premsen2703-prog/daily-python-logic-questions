total_days = int(input("Enter Total Days: "))

if total_days < 0:
    print("Total days cannot be negative.")
else:
    weeks = total_days // 7
    days = total_days % 7
    print(f"In {total_days} days there are {weeks} weeks and {days} days")