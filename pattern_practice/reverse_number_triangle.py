n = int(input("Enter n: "))

for i in range(n):
    for j in range(n,i,-1):
        print(j, end=" ")
    print()