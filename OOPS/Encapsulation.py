# Encapsulation: Binding of instance variable and methods in a single unit.

#Example 1: Differences between access modifiers:
class Person:
    def __init__(self, name, age, gender):
        self.name = name        # Public instance variable
        self._age = age         # Protected instance variable
        self.__gender = gender  # Private instance variable

class Man(Person):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)

#Example 2: Using getters and setters:

class Person2:
    def __init__(self, name, age, gender):
        self.__name = name
        self.__age = age
        self.__gender = gender
    
    def getName(self):
        return self.__name
    
    def getAge(self):
        return self.__age
    
    def getGender(self):
        return self.__gender
    
    def setAge(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Invalid age")

if __name__ == "__main__":
    man = Man("John", 30, "male")
    print(man.name)     #Output: John     # Public variable can be used publically
    print(man._age)     #Output: 30       # Protected variable can be used by derived class
    print(man.__gender) #Output: Error    # Private variable can not be accessed directly

    # Note:
    # You can use dir(class name) to see the name of the private/protected vairable,
    # You can direcly call them with those names, However that is not a good practice,
    # You neeed to use getters and setters.

    person = Person2("Johnny", 20, "male")
    print(person.getName())   #Output: Johnny  # Using getter
    person.setAge(40)         #Output: None    # Using setter
    print(person.getAge())    #Output: 20      # Using getter
