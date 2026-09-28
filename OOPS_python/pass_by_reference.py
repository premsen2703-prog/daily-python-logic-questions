class customer:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender  

def greet(customer):
    print(id(customer))
    




cust = customer("prem","male")
print(id(cust))
greet(cust)