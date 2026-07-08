n = int(input("Enter n: "))
for i in range(1,n+1):
    if i % 2 == 0 :
        print(" "*(n-i),end="")
        print("0"*(2*i-1))
    else:
        print(" "*(n-i),end="")
        print("1"*(2*i-1))
