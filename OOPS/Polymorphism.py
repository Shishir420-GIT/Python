# Example Polymorphism 1
class Animal:
    def speak(self):
        print("This animal is speaking")

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

def animal_speak(animal):
    """
    Public class, taking input as an object and calling it's specific method
    """
    animal.speak()

class Shape:
    def area():
        print("This function returns area of a shape")

class Rectangle(Shape):
    def area(self, length, breadth):
        return (length*breadth)

class Circle(Shape):
    def area(self, radius):
        return 2*3.14*radius*radius

def calc_shape_area(shape):
    """
    """
    print(shape.area())

if __name__ == "__main__":

    # Example 1
    dog = Dog()
    cat = Cat()
    cat.speak()  # Output: Meow!
    dog.speak()  # Output: Woof!

    # Using method to call specific functions
    animal_speak(dog)  # Output: Woof!
    animal_speak(cat)  # Output: Meow!  # Output: Woof!

    # Example 2
    rectangle = Rectangle()
    circle = Circle()
    print(rectangle.area(10, 20))  # Output: 200
    print(circle.area(10))  # Output: 314.0

