class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_student_details(self):
        print(self.name, self.age)

s = Student("ovi", 2)
s.print_student_details()
