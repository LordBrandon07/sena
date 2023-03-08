class Register:
    def __init__(self, document, name, age, contactnum, username, password):
        self.__document = document
        self.name = name
        self.age = age
        self.contactnum = contactnum
        self.__username = username
        self.__password = password

    def add(self):
        pass

class Student(Register):
    pass

class Instructor(Register):
    def assingSubject(self, Subject):
        Subject.assingInstructor(self)

class Enrollement:
    def enrollementCourse(student,text, course):
        return student.name,text, course.name

class Transactions:
    def pay(student):
        return student.name

class Subject:
    def __init__(self, id, name, description):
        self.__id = id
        self.name = name
        self.description = description

    def assingInstructor(self, instructor):
        self.instructor = instructor

class Course:
    def __init__(self, id, name, description, date, yearlevel):
        self.__id = id
        self.name = name
        self.description = description
        self.date = date
        self.yearlevel = yearlevel
        self.students = []
        self.instructor = []

    def enrollementStudent(self, student):
        self.students.append(student)

    def assingInstructor(self, instructor):
        self.instructor = instructor

student1 = Student(1023659663, 'pepe', 23, 320569665, 'pepe2000', '12345678')
print(f'Student: { student1.name}')

instructor1 = Instructor(23659663, 'flavio', 30, 314569665, 'flavioZZZ', '**345678')
print(f'Instructor: {instructor1.name}')

subject1 = Subject('s01', 'python', 'basic')
print('Subject: ', subject1.name)

instructor1.assingSubject(subject1)
print(f'the instructor has assigned: {subject1.instructor.name}')

course1 = Course(101, 'programming', 'lenguaje', 2023, '3 quarter')
print(f'Course: {course1.name}')

course1.assingInstructor(instructor1)
print(f'the assigned instructor is: {course1.instructor.name}')

Enrollement1 = Enrollement
print(Enrollement1.enrollementCourse(student1,'enrolled in the course', course1))

pay1 = Transactions
print(f'{pay1.pay(student1)} ha pagado la matricula')
