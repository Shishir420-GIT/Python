# These are interfaces - ABC stands for Abstract Base Class

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def drive(self):
        pass

class Car(Vehicle):
    def drive(self):
        return "Car is being driven"
    
class Motorcycle(Vehicle):
    def drive(self):
        return "Motorcycle is being driven"
    
def drive_vehicle(vehicle):
    print(vehicle.drive())

if __name__ == "__main__":
    car = Car()
    motorcycle = Motorcycle()
    drive_vehicle(car)
    drive_vehicle(motorcycle)  # Output: Motorcycle is being driven