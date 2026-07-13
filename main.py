from class_Student import Student
from class_Group import Group
from class_MyException import MyException


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')

gr = Group('PD1')

gr.add_student(st1)
gr.add_student(st2)
print(gr)

mytestname=['jobs', 'Jobs2']

for i in mytestname:
    if gr.find_student(i) == st1:
        print("Знайдено студента " + i)
    else:
        print("Не знайдено студента " + i)

gr.delete_student('Taylor')
print(gr)


