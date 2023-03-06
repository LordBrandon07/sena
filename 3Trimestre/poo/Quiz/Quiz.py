#quiz

class Register:
    def __init__(self, document, name, age, contactnum, rol, username, password):
        self.__document = document
        self.name = name
        self.age = age
        self.contactnum = contactnum
        self.rol = rol
        self.__username = username
        self.__password = password
        self.instructor = []
        self.student = []

    def add(self):
        if self.rol == 'instructor':
            self.instructor.append(self.__document)
        elif self.rol == 'student':
            self.student.append(self.__document)
        else:
            print('incorrect rol')
    
    def getupdate(self, name, age, contactnum, rol, username, password):
        self.name = name
        self.age = age
        self.contactnum = contactnum
        self.rol = rol
        self.__username = username
        self.__password = password
    
    def getInstructor(self):
        return self.instructor
    
    def getStudent(self):
        return self.student
        
    
class Instructor(Register):
    def __init__(self):
        pass
        
class Student(Register):
    def __init__(self):
        pass
    
class Subject:
    def __init__(self, id, name, description, schedule):
        self.__id = id
        self.name = name
        self.description = description
        self.schedule = schedule
        self.subjec = []
    
    def setsub(self, instructor):
        self.instructor = instructor
        self.subjec.append({self.name: instructor.name})

    def getsub(self):
        return self.subjec 
    
class Transaction:
    def __init__(self, id, details, date):
        self.__id = id
        self.datails = details
        self.date = date
        pass
    
    def processDebit(self):
        pass
    
class Enrollment:
    def __init__(self, id, details, reqeriments, date):
        self.__id = id
        self.datails = details
        self.requeriments = reqeriments
        self.date = date
        pass
    
    def setupdate():
        pass

class course:
    def __init__(self, id, description, date, yearlevel):
        self.__id = id
        self.description = description
        self.date = date
        self.yearlevel = yearlevel
        pass
    
persona1 = Register(1023659663, 'pepe', 23, 320569665, 'student', 'pepe2000', '12345678')
persona1.add()
print(persona1.getStudent())

persona2 = Register(23659663, 'flavio', 30, 314569665, 'instructor', 'flavioZZZ', '**345678')
persona2.add()
print(persona2.getInstructor())

subje1 = Subject('b101', 'art', 'paint', 'night')
subje1.setsub(persona2)
print(subje1.getsub())

