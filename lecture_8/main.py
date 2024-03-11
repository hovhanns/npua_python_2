## oop intruduction
## class and object

class Animal:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print(f"{self.name} is walking")
    
    def talk(self):
        print(f"{self.name} is talking")

# inheritence example
class Dog(Animal):
    def __init__(self, name, weight):
        super().__init__(name)
        #Animal.__init__(self, name)
        self.weight = weight

    def talk(self):
        print(f"{self.name} is talking, and weight is {self.weight} kg")

    def __str__(self):
        return f"Name: {self.name}, Weight: {self.weight}"

d  = Dog("Tommy", "German Shephard")
d.walk()
d.talk()
print(d)
