#class to demonstrate class, instance, and static methods

class Demo:
        class_var = "I am a class variable"
        def __init__(self, instance_var):
            self.instance_var = instance_var
            
# Instance Method
def show_instance(self):
    print("Instance variable:", self.instance_var)
    
# Class Method
@classmethod
def show_class(cls):
    print("Class variable:", cls.class_var)
# Static Method
@staticmethod
def greet():
    print("Hello from static method")

