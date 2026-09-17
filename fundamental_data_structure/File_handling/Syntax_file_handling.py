# Writing to a file ('w' mode overwrites, 'a' mode appends)
with open("notes.txt", "w") as file:
    file.write("Hello, World!\nLearning Practical Python.")

# Reading from a file ('r' mode)
with open("notes.txt", "r") as file:
    content = file.read()
    print(content)
