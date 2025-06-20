#super() function

class Parent:
    def __init__(self):
        print("Parent constructor")
class Child(Parent):
    def __init__(self):
        super().__init__() # Calls Parent's constructor
        print("Child constructor")
Child()