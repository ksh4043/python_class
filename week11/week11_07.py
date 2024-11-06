# base : week11_03.py
# current : week11_07.py

'''
클래스명 : Point (2d 좌표)
필요 속성 : x 위치(실수), y (실수)
'''

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


    def __str__(self):
        # 타입,인스턴스주소 문자열 반환
        # 재정의 할 때 조건, 무조건 문자열 반환
        return f"({self.x},{self.y})"


p = Point()
p = Point(1,2)
p = Point(x=1)
p = Point(y=1)
print(p.x, p.y)
print(p)

class Rectangle:
    def __init__(self, x=0, y=0, w=0, h=0):
        self.x = x
        self.y = y
        self.width = w
        self.height = h


    # 사각형의 둘레를 구해서 반환하는 메서드
    def get_round(self):
        return self.width * 2 + self.height * 2


r = Rectangle(3,5,10,5)
print(r.get_round())


class Subject:
    def __init__(self, num, nm, t=None, s=None):
        self.number = num
        self.sub = nm
        self.teacher = t
        self.score = s

# Subject()
s = Subject('001', '파이선')
s2 = Subject('001', '파이선', '이인하')

class Student:
    def __init__(self, num, nm, d, b):
        self.name = num
        self.number = nm
        self.dept = d
        self.birth = b


class Rectangle2:
    def __init__(self, s=Point(), w=0.0, h=0.0):
        self.spoint = s
        self.width = w
        self.height = h


class Rectangle3:
    def __init__(self, sp = Point(), ep = Point()):
        self.start = sp
        self.end = ep


rec = Rectangle3()
rec.start.x = 1
rec.start.y = 1

rec.end.x = 10
rec.end.y = 21










