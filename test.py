class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade  # 0 - 100

    def get_grade(self):
        return self.grade

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        value = sum([student.get_grade() for student in self.students])
        return value / len(self.students)

math = Course("Math", 2)
s1 = Student("Tim", 19, 95)
s2 = Student("Bill", 19, 75)

math.add_student(s1)
math.add_student(s2)

print(math.get_average_grade()) 