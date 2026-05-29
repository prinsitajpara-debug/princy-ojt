#class,__init__,slef

class studets:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def greet(self):
            print("hello,my name is" + self.name)
s1=studets("prinsi",21)
s1.greet()

#instance attributes

class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("prinsi")
s2 = Student("jensi")

print(s1.name)
print(s2.name)

#class attritube
class Student:
    school = "ABC School"   # class attribute

    def __init__(self, name):
        self.name = name

s1 = Student("prinsi")
s2 = Student("jensi")

print(s1.school)
print(s2.school)

#instance method

class Student:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(self.name)

s1 = Student("prinsi")
s1.show()

#class method
class Student:
    school = "ABC School"

    @classmethod
    def change_school(cls, new_name):
        cls.school = new_name

Student.change_school("XYZ School")

print(Student.school)

#static method
class Math:
    
    @staticmethod
    def add(a, b):
        return a + b

print(Math.add(2, 3))

#__str__
class Student:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Student: {self.name}"

s = Student("John")

print(s)

#__repr__
class Student:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Student('{self.name}')"

s = Student("John")

print(repr(s))