class student:
    #1. static (class) variable - share by all students
    _school_name = "Global High School"

    def __init__(self, name, age):
        self.name = name
        self.age = age
# creating separate objects (instances)
student1 = student("kajal",15)
student2 = student("sujal",20)

#Accessing Instance variable 
print(student1.name,student1.age)
print(student2.name,student2.age)

#Accessing static variables
# using class_name.staticvariable_name we can acces static variable.
print(student._school_name) 
# static variable can access by using object_name.staticvariable_name.
print(student1._school_name)