#traversing string using for loop in O(n) time complexity
def find_char_instring(string,char):
    for ch in string:
        if char == ch:
            return True
    return False

if __name__ == "__main__":
    string = "hello world"
    char = "x"
    if find_char_instring(string, char):
        print(f"The character '{char}' is present in string.")
    else:
        print(f"The character '{char}' is not present in string.")