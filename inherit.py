# Filename : inherit.py


class SchoolMember:
    """Represents any school member."""
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(initialized SchoolMember: %s)' % self.name)

    def tell(self):
        """Tell my details."""
        print('Name:"%s" Age:"%s"' % (self.name, self.age), end=' ')


class Teacher(SchoolMember):
    """Represents a teacher"""
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(initialized teacher: %s)' % self.name)

    def tell(self):
        SchoolMember.tell(self)
        print('My salary is %d.' % self.salary)

class Student(SchoolMember):
    """Represent a student"""
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(initialized student: %s)' % self.name)

    def tell(self):
        SchoolMember.tell(self)
        print('My marks is %d.' % self.marks)

t = Teacher('Mrs. Shrivadya', 40, 30000)
s = Student('Swaroop', 22, 85)

print()

members = [t, s]
for member in members:
    member.tell()
