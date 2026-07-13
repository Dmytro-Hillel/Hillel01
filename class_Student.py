from class_human import Human

class Student(Human):

    def __init__(self, gender:str, age:int, first_name:str, last_name:str, record_book:str):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return "Student " + super().__str__()

    def __eq__(self, other):
        if not isinstance(other, Student):
            return False
        return self.last_name.lower() == other.last_name.lower()

    def __hash__(self):
        return hash(str(self))
