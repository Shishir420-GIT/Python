# class Circle:
#     pi = 3.14159
    
#     @classmethod
#     def calculate_area(cls, radius):
#         return cls.pi * radius * radius
#     @staticmethod
#     def calculate_area2(self, radius):
#         return self.pi * radius * radius

# # Calling the class method

# area = Circle.calculate_area(5)

# print("Area of the circle:", area)

# # Calling the static method

# area = Circle.calculate_area2(5)

# print("Area of the circle:", area)

# class Rectangle:
#     length = 0
#     width = 0
    
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
        
#     @classmethod
#     def create_square(cls, side):
#         return cls(side,side)

# # Creating a square using the class method
# square = Rectangle.create_square(5)
# print(square)
# print("Square length:", square.length)
# print("Square width:", square.width)

class Counter:
    count = 0
    def __init__(self):
        Counter.count += 1
    @classmethod
    def get_count(cls):
        return cls.count

# Creating instances of the class
c1 = Counter()
c2 = Counter()
c3 = Counter()

# Accessing the class attribute using the class method
print("Count:", Counter.get_count())


class A: pass
class B(A): pass
class C(A): pass
class D(B, C): pass

print(D.mro())  # Outputs the order in which methods are resolved

print(Counter.mro())


def outer():
    x = 5
    def inner():
        nonlocal x
        x = 10
    inner()
    print(x)  # Outputs: 10

outer()


for i in range(3):
    print(i+1,end=": ")
    for j in range(4,7):
        print(j,end=",")
    print()

