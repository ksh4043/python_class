# week05_02.py

toeic = int(input("TOEIC"))
age = int(input("AGE"))
grade = int(input("GRADE"))
temp = int(input("TEMP"))
height = int(input("HEIGHT"))

a = toeic >= 800 and age < 30
b = toeic >= 800 or age < 30
c = temp < 10 or temp > 28

d = not (age == 30) and toeic < 600
# d = (age != 30) and toeic < 600


e = height >= 120 and height <= 160
# e = 120 <= height <= 160

print(a, b, c, d, e)
