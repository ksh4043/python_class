# week11_04.py

class Student:
    def __init__(self):
        self.name = ""
        self.number = ""
        self.dept = ""
        self.birth = 0


stu1 = Student()
stu2 = Student()

stu1.name = input("이름 입력 : ")
stu1.number = input("학번 입력 : ")
stu1.dept = input("학과 입력 : ")
stu1.birth = int(input("생년 입력 : "))

stu2.name = input("이름 입력 : ")
stu2.number = input("학번 입력 : ")
stu2.dept = input("학과 입력 : ")
stu2.birth = int(input("생년 입력 : "))


print(stu1.name, stu2.name)

students = []
for i in range(3):
    stu = Student()
    stu.name = input("이름 입력 : ")
    stu.number = input("학번 입력 : ")
    stu.dept = input("학과 입력 : ")
    stu.birth = int(input("생년 입력 : "))
    students.append(stu)

for i in students:
    print(i.name)



