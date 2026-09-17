

string ="ABACABA"
pattern = "ABA"

m = len(pattern)
n = len(string)
lps = [0]*m
lenght = 0
i = 1
while i < m:
    if pattern [i] == pattern[length]:
        length +=1
        lps[i] = length
        i +=1
    else:
        if length != 0:
            length = lps[length -1]








