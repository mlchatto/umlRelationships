class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

student1 = Person("Moira", 14)

print(f"Name: {student1.name}")
print(f"Age: {student1.age}")

print("\n|------------------------------------------------------|\n")

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age

student1 = Person("Moira", 14)

print(f"Name: {student1.name}")
print(f"Age: {student1.get_age()}")

#Reflection: Accessing the age attribute through a getter method makes the code more secure and smooth. It allows for better control over how the age attribute is accessed and modified, preventing direct manipulation of the attribute from outside the class. This encapsulation helps maintain the integrity of the data and can also allow for additional logic to be added in the getter method if needed in the future. 