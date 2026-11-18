from pathlib import Path


def readfileandfolder():
    path = Path('')
    items = list(path.rglob("*"))
    for i , items in enumerate(items):
        print(f"{i+1} : {items} ")

def createfile():
    try:
        readfileandfolder()
        name = input("Please tell your file name: ")
        file = Path(name)
        if not file.exists():
            with open(file,"w")as content:
                data = input("what  you want to write in this file: ")
                content.write(data)
            print(F"File created sucessfully")
        else:
            print("this file already exists")
    except Exception as Error:
        print(f"An Error occured as {Error}")

def readfile():
    try:
        readfileandfolder()
        name = input("which file you wnat to create: ")
        file = Path(name)
        if file.exists() and file.is_file():
            with open(file,"r")as content:
                data = content.read()
                print(data)
            print("Readed sucessfully")
        else:
            print print("File is already exist")
    except:
        
        
     





print("press 1 for reading a file")
print("press 2 for writing  a file")
print("press 3 for updating a file")
print("press 4 for deletion a file")

check = int(input("tell me your respose: "))

if check == 1:
    createfile()
if check == 2:
    readfile()
