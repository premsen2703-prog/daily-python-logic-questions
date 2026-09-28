#collection of objects means when you are able to place objects inside a list,tuple,or dict. 
class customer:
    def __init__(self,name, age):
        self.name = name
        self.age = age  

    def intro(self):
        print("I am", self.name,"and i am",self.age)



c1 = customer("prem",21)
c2 = customer("sujal",23)
c3 = customer("priya",20)

l = [c1,c2,c3]
for i in l:
    print(i.name,i.age)