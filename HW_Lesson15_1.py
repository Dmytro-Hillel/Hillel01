class MyException(Exception):
    pass

class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return self.first_name + " " + str(self.last_name)

class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return "Student " + super().__str__()

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
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        strout = "Group" + " " + self.number + "\n"
        for student in self.group:
            strout = strout + "\t" + str(student) + "\n"
        return strout


mygr = Group("GR1")
for item in range(10):
    mygr.add_student(Student("Male", 20, "student"+str(item), "student"+str(item), "AG88"+str(item)))
print(mygr)

try:
    mygr.add_student(Student("Male", 20, "student"+"11", "student"+"11", "AG88"+"11"))
except MyException as e:
    print(e)

