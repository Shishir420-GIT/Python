# Abatraction: Hiding complex implementation or just implementations of a class and displaying just what is needed.
from abc import ABC,abstractmethod

class Vehicle(ABC):
    def drive(self): # Not an abstract doesn't need forced implementation
        return "Vehicle is not being Driven"
    
    @abstractmethod
    def start(self): # Abstract class needs forced implementation
        pass

class Auto(Vehicle):
    def start(self):
        return "Auto is being started"

if __name__ == "__main__":
    auto = Auto()
    print(auto.start())
    print(auto.drive())
