class parent:
    def parent_method(self):
        print("parent")

class child(parent):
    def parent_method(self):
        print("adarsh")

    def child_method(self):
        print("parent")
        super().parent_method()

c1 = child()
c1.parent_method()
c1.child_method()

# super keyword is used to access methods of parent class
# sometimes methods have common names
