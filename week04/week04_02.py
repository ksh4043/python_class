# week04_02

data1 = [1, 2, 3, 4, 5]
data2 = [1, 2, 3, ['a', 'b', 'c']]

print(data1[0]) # 1
print(data1[-1]) # 5
print(data1[0] + data1[-1]) # 1 + 5 = 6
print(data1[:2]) # [1, 2]
print(data1[2:]) # [3, 4, 5]
print(data1[2:-1]) # [3, 4]

print()
print(data2[0], type(data2[0])) # 1 int
print(data2[-1], type(data2[-1])) # ['a', 'b', 'c'] list
print(data2[-1][-1], type(data2[-1][-1])) # 'c' str
print(data2[2:], type(data2[2:])) # [3, ['a', 'b', 'c']] list
print(data2[3][1], type(data2[3][1])) # 'b' str
print(data2[3][:2], type(data2[3][:2])) # ['a', 'b'] list
