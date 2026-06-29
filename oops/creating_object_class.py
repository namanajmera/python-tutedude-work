
class MyClass:
    pass

obj1 = MyClass()
obj2 = MyClass()

print(type(obj1))


class Student:
    """
    This is a class Student to manage student information.
    """
    pass

student1 = Student()
student2 = Student()

student1.name = "Naman"
student1.roll = 1001;

print(Student.__doc__)
print(help(Student))

print(student1.name)
print(student1.roll)

print(student1.__dict__)
print(student2.__dict__)