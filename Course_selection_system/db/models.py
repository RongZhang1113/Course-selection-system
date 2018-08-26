from db import handler


class BaseClass:
    def save(self):
        handler.save(self)

    @classmethod
    def get_obj_from_name(cls, name):
        return handler.query(name, cls.__name__.lower())


class Admin(BaseClass):
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.save()

    def create_school(self, name, address):
        School(name, address)

    def create_teacher(self, name, password):
        Teacher(name, password)

    def create_course(self, name):
        Course(name)


class School(BaseClass):
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.courses = []
        self.save()

    def add_course(self, name):
        self.courses.append(name)
        self.save()


class Teacher(BaseClass):
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.courses = []
        self.save()

    def add_course(self, name):
        self.courses.append(name)
        self.save()

    def modify_score(self, student, cour_name, score):
        student.scores[cour_name] = score
        student.save()


class Student(BaseClass):
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.courses = []
        self.school = None
        self.scores = {}
        self.save()

    def get_school(self):
        return self.school

    def choose_school(self, name):
        self.school = name
        self.save()

    def choose_course(self, name):
        self.courses.append(name)
        self.scores[name] = 0
        self.save()


class Course(BaseClass):
    def __init__(self, name):
        self.name = name
        self.students = []
        self.save()

    def add_student(self, name):
        self.students.append(name)
        self.save()
