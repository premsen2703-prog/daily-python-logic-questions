class teacher:
    surname = "mam"
    def __init__(self,name):
        self.name = name # these are the dynamic variables different for every object.
        
t1 = teacher("anshu")
print(id(t1))
print(t1.name)

