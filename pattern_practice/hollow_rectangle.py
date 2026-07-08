rows = int(input("Enter number of rows: "))
column = int(input("Enter number of columns: "))
for i in range(rows):
    for j in range(column):
        if i == 0 or i == rows - 1 or j == 0 or j == column-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()