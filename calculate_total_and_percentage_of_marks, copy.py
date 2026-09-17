subject1 = float(input("enter marks of subject1: "))
subject2 = float(input("enter marks of subject2: "))
subject3 = float(input("enter marks of subject3: "))
total = subject3 + subject2 + subject1
percentage = (total/ 300) * 100
print(f"Total of marks: {total}")
print(f"percentage of marks = {percentage:.2f}%")
