# week12_01.py

class Subject: # Subject() 호출 시 __new__() 호출 및 생성 --> __init__()
    def setGrade(self, grade):
        if grade != None and (grade < 0 or grade > 4.5):
            grade = None
        self.grade = grade

    
    def __init__(self, number, name, teacher=None, grade=None):
        self.number = number
        self.name = name
        self.teacher = teacher
        self.setGrade(grade)


    def __str__(self):
        return f"[{self.number}] {self.name}"

"""
sub = Subject("CS0001", "컴퓨터개론", grade=100.9)
print(sub.grade)

sub = Subject("CS0001", "컴퓨터개론", grade=100.9)
sub.setGrade(100.9)
print(sub.grade)

sub = Subject("CS0001", "컴퓨터개론")
print(sub.grade)
"""

class Student:
    def totalGrade(self):
        if self.subjects:
            grades = [sub.grade for sub in self.subjects if sub.grade != None]
            if grades:
                return sum(grades) / len(grades)
        else:
            # print("수강 과목이 없어")
            return None # python은 기본적으로 None을 리턴함

    
    def __init__(self, number, name, dept, birth_year, *subjects):
        self.number = number
        self.name = name
        self.dept = dept
        self.birth_year = birth_year
        if subjects:
            self.subjects = list(subjects)
        else:
            self.subjects = list()
        # *subjects > tuple 형태기 때문에 list로 캐스팅해서 핸들링하기 쉽게 함


    def __str__(self):
        return f"[{self.number}] {self.name}"


st = Student("1", "김시현", "컴정", 2024)
print(st)
print(st.totalGrade())


st = Student("2", "박수빈", "컴정", 2024
             , Subject("001", "파이썬", "김인하")
             , Subject("002", "자바스크립트", "전혜경")
             )
print(st)
print(st.totalGrade())

st = Student("3", "김은혜", "컴정", 2024
             , Subject("001", "파이썬", "김인하", grade = 4.5)
             , Subject("002", "자바스크립트", "전혜경")
             , Subject("002", "오픈소스프로그래밍", "김태간", grade = 4.0)
             )
print(st)
print(st.totalGrade())






