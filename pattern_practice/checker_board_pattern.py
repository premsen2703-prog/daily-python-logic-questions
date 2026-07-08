n = int(input("Enter n : "))
for i in range(n):
    for j in range(n+1):
        if (i+j)% 2==0:
            print("*",end="")
        else:
            print(" ",end="")
    print()