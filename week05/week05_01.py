# week05_01.py

class Test:
    def __init__(self):
        self.a=1
        self.b=2

test1 = [1, 2]
test2 = (1, 2)
test3 = Test()

print(test1[0])
print(test2[0])
print(test3.a)

print(test1[1])
print(test2[1])
print(test3.b)

test1[0] = 3
#test2[0] = 3
test3.a = 3
print(test1[0])
#print(test2[0])
print(test3.a)
