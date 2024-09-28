# week04_03.py

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
d = [a, b]

print(a) # [1, 2, 3]
print(b) # [4, 5, 6]
print(c) # [1, 2, 3, 4, 5, 6]
print(d) # [[1, 2, 3], [4, 5, 6]]

e = a * 3
print(e) # [1, 2, 3, 1, 2, 3, 1, 2, 3]
print(len(b)) # 3
print(len(c)) # 6
print(len(d)) # 2
