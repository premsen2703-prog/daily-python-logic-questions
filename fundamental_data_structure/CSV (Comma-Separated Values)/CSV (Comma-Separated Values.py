import csv

# Writing to a CSV file
with open("users.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Role", "ID"])  # Header row
    writer.writerow(["Bob", "Developer", "101"])

# Reading from a CSV file
with open("users.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)  # Each row is a list of strings
