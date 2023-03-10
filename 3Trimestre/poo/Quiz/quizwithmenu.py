class Register:
    def __init__(self, document, name, age, contactnum, username, password):
        self.__document = document
        self.name = name
        self.age = age
        self.contactnum = contactnum
        self.__username = username
        self.__password = password

    def getData(self):
        return self.__document, self.name, self.age, self.contactnum, self.__username, self.__password
    
    def setAge(self, age):
        self.age = age

    def setContactum(self, contactnum):
        self.contactnum = contactnum

    def setPassword(self, password):
        self.__password = password

class Student(Register):
    pass

class Instructor(Register,):
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

    def getDatosSubject(self):
        return self.__id, self.name, self.description

class Course:
    def __init__(self, id, name, description, date, yearlevel):
        self.__id = id
        self.name = name
        self.description = description
        self.date = date
        self.yearlevel = yearlevel

    def enrollementStudent(self, student):
        self.students.append(student)

    def assingInstructor(self, instructor):
        self.instructor = instructor

    def getDatosCourse(self):
        return self.__id, self.name, self.description, self.date, self.yearlevel
    
    def setName(self, name):
        self.name = name

    def setDescription(self, description):
        self.description = description

    def setDate(self, date):
        self.date = date

    def setYearlevel(self, yearlevel):
        self.yearlevel = yearlevel

# student1 = Student(1023659663, 'pepe', 23, 320569665, 'pepe2000', '12345678')
# print(f'Student: { student1.name}')

# instructor1 = Instructor(23659663, 'flavio', 30, 314569665, 'flavioZZZ', '**345678')
# print(f'Instructor: {instructor1.name}')

# subject1 = Subject('s01', 'python', 'basic')
# print('Subject: ', subject1.name)

# instructor1.assingSubject(subject1)
# print(f'the instructor has assigned: {subject1.instructor.name}')

# course1 = Course(101, 'programming', 'lenguaje', 2023, '3 quarter')
# print(f'Course: {course1.name}')

# course1.assingInstructor(instructor1)
# print(f'the assigned instructor is: {course1.instructor.name}')

# Enrollement1 = Enrollement
# print(Enrollement1.enrollementCourse(student1,'enrolled in the course', course1))

# pay1 = Transactions
# print(f'{pay1.pay(student1)} ha pagado la matricula')

def prueba():
    while True:
        print('''
            menu

    1- Register student
    2- View student
    3- Register instructor
    4- View instructor
    5- Assign subject
    6- View subject
    7- Create course
    8- View course
    9- Enrollement
    10- Pay
    00- other menu
    0- Exit
        ''')

        selection = int(input('Select your option: '))     
        if selection == 1:
            document = input('Enter your document:')
            name = input('Enter your name: ')
            age = input('Enter your age: ')
            contactnum = input('Enter your contactnum: ')
            username = input('Enter your username: ')
            password = input('Enter your password: ')
            student1 = Student(document, name, age, contactnum, username, password)
            print(f'Registered student: { student1.name}')

        elif selection == 2:
            print(student1.getData())

        elif selection == 3:
            document1 = input('Enter your document:')
            name1 = input('Enter your name: ')
            age1 = input('Enter your age: ')
            contactnum1 = input('Enter your contactnum: ')
            username1 = input('Enter your username: ')
            password1 = input('Enter your password: ')
            instructor1 = Instructor(document1, name1, age1, contactnum1, username1, password1)
            print(f'Registered instructor: { instructor1.name}')

        elif selection == 4:
            print(instructor1.getData())

        elif selection == 5:
            id = input('Enter the subject id: ')
            name2 = input('Enter the subject name: ')
            description = input('Enter the subject description: ')
            subject1 = Subject(id, name2, description)
            print(f'New subject: {subject1.name}')
            sesub = int(input('do you want to assign the subject to the instructor: y=1/n=2: '))
            if sesub == 1:
                instructor1.assingSubject(subject1)
                print(f'the assigned instructor: {subject1.instructor.name}, to the subject {subject1.name} ')
            elif sesub == 2:
                print('ok')
            else:
                print('Incorrect data')

        elif selection == 6:
            print(subject1.getDatosSubject())

        elif selection == 7:
            id3 = input('Enter the course id: ')
            name3 = input('Enter the course name: ')
            description3 = input('Enter the course: ')
            date3 = input('Enter the course date: ')
            yearlevel3 = input('Enter the course yearlevel: ')
            course1 = Course(id3, name3, description3, date3, yearlevel3)
            print(f'Course: {course1.name}')

        elif selection == 8:
            print(course1.getDatosCourse())

        elif selection == 9:
            enrollement1 = Enrollement
            print(enrollement1.enrollementCourse(student1,'enrolled in the course', course1))
        elif selection == 10:
            pay1 = Transactions
            print(f'{pay1.pay(student1)} hes paid the registration')
        elif selection == 11:
            pass

        elif selection == 0:
            exit()

        else:
            print('Incorrect data')

prueba()