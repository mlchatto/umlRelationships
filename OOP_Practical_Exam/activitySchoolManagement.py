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

print("\n|------------------------------------------------------|\n")

class Student(Person):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)

    def study(self):
        print(f"{self.name} is studying.")

student2 = Student("Martha", 15)

print(f"Name: {student2.name}")
print(f"Age: {student2.get_age()}")

student2.study()

print("\n|------------------------------------------------------|\n")

class Teacher(Person):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)

    def teach(self):
        print(f"{self.name} is teaching.")

teacher1 = Teacher("Mona", 30)

print(f"Name: {teacher1.name}")
print(f"Age: {teacher1.get_age()}")

teacher1.teach()