#Single and Multilevel Inheritance

# Base class
class Animal:
    def speak(self):
        print("Animal makes a sound")
        
# Single Inheritance: Dog inherits from Animal
class Dog(Animal):
    def bark(self):
        print("Dog barks")
        
# Multilevel Inheritance: Puppy inherits from Dog (which inherits from Animal)
class Puppy(Dog):
    def weep(self):
        print("Puppy weeps softly")
        
# ----- Testing Single Inheritance -----
print("=== Single Inheritance Example ===")
dog = Dog()
dog.speak() 
dog.bark() 

# ----- Testing Multilevel Inheritance -----
print("\n=== Multilevel Inheritance Example ===")
puppy = Puppy()
puppy.speak() 
puppy.bark() 
puppy.weep()