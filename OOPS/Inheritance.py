#Passing on the properties and methods to another class by inhereting it.

# Example Single Parent Inheritance:
class Car:
    owner = ""
    windows = 0
    def __init__(self, owner, windows):
        self.owner = owner
        self.windows = windows
    
    def drive(self):
        print(f"{self.owner} is driving the car.")

class Tesla(Car):
    battery = False
    model = ""
    def __init__(self, owner, windows, model, battery) -> None:
        super().__init__(owner, windows)
        self.model = model
        self.battery = battery

 # Example Multiple Parent Inheritance:
class Animals:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def walk(self):
        print(f"{self.name} is walking from Animals Class.")

class Pet:
    def __init__(self, owner):
        self.owner = owner
    def speak(self):
        print(f"{self.name} says hello from Pet Class.")

class Puppy(Animals,Pet):
    def __init__(self, owner, name, age):
        Animals.__init__(self, name, age)
        Pet.__init__(self, owner)


if __name__ == "__main__":

    # Example Single Parent Inheritance:
    tesla = Tesla("John", 4, "Model S", True)
    tesla.drive()  # Output: John is driving the car.

    # Example Multiple Parent Inheritance:
    puppy = Puppy("John", "Buddy", 1)
    puppy.walk()  # Output: Buddy is walking.
    puppy.speak()  # Output: Buddy says hello.




