# week04_11.py

class Student:
    def __init__(self):
        self.name = ""
        self.numer = ""
        self.dept =  ""
        self.year = 0
    def __str__(self):
        return f"{self.name}/{self.number}/{self.dept}/{self.year}"

stu = Student()
stu.name = input("이름:")
stu.number = input("학번:")
stu.dept = input("학과:")
stu.year = int(input("생년:"))

print(stu)



class Subject:
    def __init__(self):
        self.number = ""
        self.name = ""
        self.teacher = ""
        self.credit = 3



class Ractangle:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        self.width = 0.0 
        self.height = 0.0

r = Ractangle()
r.x = 5.0
r.y = 6.0
r.width = 10
r.height = 5



class Point:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0

p1 = Point()
print(p1.x, p1.y)

p2 = Point()
p2.x = -1.0
p2.y = 4.1
print(p1.x, p1.y)
print(p2.x, p2.y)
