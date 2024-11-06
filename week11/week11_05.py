# week11_05.py

class Test:
    def __init__(self):
        self.name = None
        self.age = None
    
    def func(self, name, age):
        self.name = name
        print(age)

        
t = Test()
print(t.name)
print(t.age)

t = Test()
t.func("김인하", 20)
print(t.name)
print(t.age)

print("-" * 20)

class In:
    def func(self):
        print("In.func()")


class Out:
    def method(self):
        print("Out.method()")


# 안되면 주석
# method()
# func()

# Out.method()
# In.func()

i = In()
o = Out()

# 정식표현 (실제로 잘 안 쓴다)
Out.method(o)
In.func(i)

# 약식표현 (실제로 쓰는)
i.func()
o.method()

# 되지만 정상 작동하지 않을 가능성이 큼
In.func(o)
Out.method(i)

# 아예 실행 X
# i.method()
# o.func()
