class Parent:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def display(self):
        print(self.name, self.id)

class Child(Parent):
    print("the child class")

c1 = Child("mayank", 201)
c1.display()

# parent class -> display
# child class inherits the display method