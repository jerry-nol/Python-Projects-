

#Parent class
class User:
    name = 'Luke'
    email = 'cambell@gmail.com'
    password = 'coding321'

    def userInfo(self):
        enterName = input('\nPlease enter name: ')
        enterEmail = input('\nPlease enter email: ')
        enterPasscode = input('\nPlease enter password: ')

        if(enterEmail == self.email and enterPasscode == self.password):
            print("Hello {}, welcome!".format(enterName))
        else:
            print('Invalid, please try again')

#Child class Student
class Student(User):
    number_of_classes = 4
    GPA = 3.0
    studentID = '4858'

    #Using the same function as before but changing the passcode to student ID

    def userInfo(self):
        enterName = input('\nPlease enter name: ')
        enterEmail = input('\nPlease enter email: ')
        enterStudentID = input('\nPlease enter your Student ID: ')

        if(enterEmail == self.email and enterStudentID == self.studentID):
            print("Hello {}, welcome!".format(enterName))
        else:
            print('Invalid, please try again')

#Child class Teacher
class Teacher(User):
    numberOfStudents = 40
    lecturesPerDay = 5
    teacherID = '8485'
    department = 'History'
    
    #Instead of using student id or passcode its asking for teacher id
    def userInfo(self):
        enterName = input('\nPlease enter name: ')
        enterEmail = input('\nPlease enter email: ')
        enterTeacherID = input('\nPlease enter your Teacher ID: ')

    if(enterEmail == self.email and enterTeacherID == self.teacherID):
        print("Hello {}, welcome!".format(enterName))
    else:
        print('Invalid, please try again')
    

    

