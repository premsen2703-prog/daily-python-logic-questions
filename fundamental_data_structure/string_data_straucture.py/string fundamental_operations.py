#creating a string
string = "hello world"
#accessing character of string 
print(string[0])  # Output: h
#find the length of string by using built-in len() function 
print(len(string))  # Output: 11
#find the length of string by using for loop 
def stringlength(string):
    count = 0
    for ch in string:
        count += 1
    return count

s = "hello world"
print(stringlength(s))  # Output: 11

#
