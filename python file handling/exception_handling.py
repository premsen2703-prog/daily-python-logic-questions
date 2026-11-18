try:
    file = open("emptyfile.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError as e:
    print("Error :",e)
finally:
    file.close()
    