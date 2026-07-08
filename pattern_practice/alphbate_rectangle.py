rows = int(input("Enter number of rows: "))
column = int(input("Enter number of columns: "))
for i in range(1,rows+1):
    for j in range(column):
        print(chr(64+i),end="")
    print()
