n = int(input("Enter n: "))
for i in range(1,n+1):
    #loop for printing spaces
    print(" "*(n-i),end="")
    #lop for printing stars
    for j in range(1,2*i):
        if j == 1 or j == 2*i-1 or i == n:
            print("*",end="")
        else:
            print(" ",end="")
    print()