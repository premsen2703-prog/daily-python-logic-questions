class customer:
    def __init__(self,name):
        self.name = name
        print(id(self))



customer("prem") #here object is lost not stored in any variable.
#here cust is the variable called reference variable because it stroes the refence address of object.
cust = customer("sujal")