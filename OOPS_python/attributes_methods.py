class smartphone:
    def __init__(self):
        self.model = "iphone 15" #Attribute
        
    def ring(self): # Method
        return "BEEP BEEP!"


iphone = smartphone()
print(iphone.model)# calling class attribute
print(iphone.ring())# calling class method
