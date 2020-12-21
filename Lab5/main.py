# from ZODB import FileStorage, DB
# storage = FileStorage.FileStorage('mydatabase.fs')
# db = DB(storage)
# connection = db.open()
# root = connection.root()
# root['employees'] = ['Mary', 'Jo', 'Bob']
# import transaction
# transaction.commit()
# connection.close()
from ZODB import FileStorage, DB
from Student import Student
from datetime import datetime
import transaction


def createStudent():
    print("Input retiree's info")
    firstname = input("First name: ")
    lastname = input("Last name: ")
    birthday = input("Birthday date(day, month, year(two last digits)): ")
    faculty = input("Faculty: ")
    group = input("Group: ")
    averagescore = input("Average score: ")
    grant = input("Grant: ")

    return Student(firstname, lastname, datetime.strptime(birthday, '%d,%m,%y'), faculty, group, averagescore, grant)


def printStudent(Student):
    print(Student.firstname + " " + Student.lastname + " " + Student.group)


i = 0
count = 0
minscore = 5.0
students = {}
storage = FileStorage.FileStorage('mydatabase.fs')
db = DB(storage)
connection = db.open()
students = connection.root()
while (True):
    text = input("Do you want add new player?(Yes, No): ")
    if (text == "No"):
        break

    if (text != "Yes"):
        print("Invalid input")
        continue

    info = createStudent()
    students[i] = info
    transaction.commit()
    i = 1 + i
    if text == "No" and info is not None:
        connection.close()

for x in students:
    student = students[x]
    count += 1
    if minscore > float(student.averagescore):
        minscore = float(student.averagescore)
        i = count
printStudent(students[i])
print(minscore)
print("Count students " + str(count))
