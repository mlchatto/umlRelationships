class Student:
  def __init__(self, name: str):
    self.name = name

class Class:
  def __init__(self, students: list(Student) = None):
    self.students = students if students else []

student1 = Student("RJ")
student2 = Student("AV")

xenon = Class([student1, student 2])
print(xenon)
