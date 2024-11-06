# week11_02.py
import datetime

class Test:
    def __init__(self): # local value
        self.name = "a" # attribute / member(instance) variable
        self.age = 20   # 상동
        print(datetime.datetime.now())

t = Test()
print(t.name)

t2 = Test()
print(t.name)

t.name = "김인하"
t2.name = "이인하"

print(id(t), id(t2))
print(type(t) == type(t2))
print(t == t2)
print(t.name == t2.name)
print(t.age == t2.age)
