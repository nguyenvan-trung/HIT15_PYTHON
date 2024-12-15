class Student:
    def __init__(self,name, yob, grade):
        self.name= name
        self.yob = yob
        self.grade = grade

    def describe(self):
        print("student-name: ",self.name)
        print(" nam sinh-yob la: ", self.yob)
        print(" diem thi-grade la: ", self.grade)

class Doctor:
    def __init__(self,name, yob,specialist):
        self.name= name
        self.yob = yob
        self.specialist = specialist

    def describe(self):
        print("doctor-name: ",self.name)
        print(" nam sinh-yob la: ", self.yob)
        print(" chuyen mon-specialist: ", self.specialist)

class Teacher:
    def __init__(self, name,yob,subject):
        self.name= name
        self.yob = yob
        self.subject = subject

    def describe(self):
        print("teacher-name: ", self.name)
        print(" nam sinh-yob la: ", self.yob)
        print(" chuyen mon-subject: ", self.subject)
    
class Ward:
    def __init__(self, name):
        self.name = name
        self.people = []  

    def addPerson(self, person):
        self.people.append(person)

    def describe(self):
        print(f"\nWard Name: {self.name}")
        for person in self.people:
            person.describe()
            print()

student1 = Student(name="studentA", yob=2010, grade="7")
# student1.describe()
teacher1 = Teacher(name="teacherA", yob=1969, subject="Math")
# teacher1.describe()
doctor1 = Doctor(name="doctorA", yob=1945, specialist="Endocrinologists")
# doctor1.describe()
teacher2 = Teacher(name="teacherB", yob=1995, subject="History")
doctor2 = Doctor(name="doctorB", yob=1975, specialist="Cardiologists")
ward1 = Ward(name="Ward1")
ward1.addPerson(student1)
ward1.addPerson(teacher1)
ward1.addPerson(teacher2)
ward1.addPerson(doctor1)
ward1.addPerson(doctor2)
ward1.describe()