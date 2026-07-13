# from class_Student import Student
from class_MyException import MyException

class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()
        self.max_students = 10

    def add_student(self, student):

        if len(self.group) == self.max_students:
            raise MyException("Максимальна кількість студентів")

        new_stud = self.find_student(student.last_name)
        if new_stud is None:
            self.group.add(student)
        else:
            print("Студент вже є в групі")

    def delete_student(self, last_name):
        del_item = self.find_student(last_name)
        if del_item:
            self.group.remove(del_item)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name.lower() == last_name.lower():
                return student
        return None

    def __str__(self):
        strout = "Group" + " " + self.number + "\n"
        for student in self.group:
            strout = strout + "\t" + str(student) + "\n"
        return strout