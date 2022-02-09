class Student:

    def __init__(self, fname, lname):
        self._firstname= fname
        self._lastname= lname

    def students(self):
        return f'{self._firstname}, {self._lastname}'

name = Student("isai", "mar")
print(name.students())