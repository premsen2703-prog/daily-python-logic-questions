#Inheritance
class animal:
    def eat(self):
        return "chomp"

class cat(animal):
    def meow(self):
        return "Meow"

loin = animal()
print(cat())