# week11_03.py

'''
클래스명 : Point (2d 좌표)
필요 속성 : x 위치(실수), y (실수)
'''

class Point:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0


p = Point()
print(p.x, p.y)

class Rectangle:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        self.width = 0.0
        self.height = 0.0


r = Rectangle()

class Subject:
    def __init__(self):
        self.number = ""
        self.sub = ""
        self.teacher = ""
        self.score = 0.0


s = Subject()

class Student:
    def __init__(self):
        self.name = ""
        self.number = ""
        self.dept = ""
        self.birth = 0


stu = Student()

class Rectangle2:
    def __init__(self):
        self.spoint = Point()
        self.width = 0.0
        self.height = 0.0


class Rectangle3:
    def __init__(self):
        self.start = Point()
        self.end = Point()


rec = Rectangle3()
rec.start.x = 1
rec.start.y = 1

rec.end.x = 10
rec.end.y = 21










