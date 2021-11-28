# zad 1

class Student:
    def __init__(self, name: str, marks: int):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f'{self.name}'

    def is_passed(self):
        if self.marks > 50:
            return True
        else:
            return False


obj1 = Student(name='Ktoś', marks=0)
obj1.marks = 51
print(obj1.is_passed())
obj1.marks = 49
print(obj1.is_passed())
