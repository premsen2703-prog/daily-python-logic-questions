n = int(input("Enter n: "))
for i in range(n,-1,-1):
    print(" "*(n-i),end="")
    print(chr(65+i)*(2*i+1))
