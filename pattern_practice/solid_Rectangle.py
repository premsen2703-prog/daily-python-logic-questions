rows= int(input("enter number of rows: "))
column = int(input("enter number of columns: "))

for i in range(rows):
    for j in range(column):
        print("*",end="")
    print()