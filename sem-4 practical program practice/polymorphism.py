#polymorphism

class Cat:
    def speak(self): print("Meow")
    
class Dog:
    def speak(self): print("Bark")
    
for animal in [Cat(), Dog()]:
    animal.speak() # Same method, different behavior