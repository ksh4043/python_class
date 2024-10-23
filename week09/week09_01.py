# week09_01.py

data1 = [1, 2, 3, 4]

summary = sum(data1)
maximum = max(data1)
minimum = min(data1)
average = summary / len(data1)

print(summary)
print(maximum)
print(minimum)
print(average)

print("-" * 30)

for i in data1:
    print(i)

print("-" * 30)

for i in range(len(data1)):
    print(i)

print("-" * 30)

for i in range(len(data1)):
    print(f"data1[{i}] : {data1[i]}")

print("-" * 30)

for v in enumerate(data1):
    print(f"data1[{v[0]}] : {v[1]}")

print("-" * 30)

for i,v in enumerate(data1):
    print(f"data1[{i}] : {v}")

data2 = [
    [1,2,3]
    ,[10,20]
    ,[11,12,13,14]
    ]

print("-" * 30)

for i in data2:
    print(i)

print("-" * 30)

for i in data2:
    print("sum", sum(i))
    print("max", max(i))
    print("min", min(i))
    print("avg", sum(i) / len(i))

print("-" * 30)

for i in range(len(data2)):
    print(f"{i+1}번째 : {data2[i]}")
    print("sum", sum(data2[i]))
    print("max", max(data2[i]))
    print("min", min(data2[i]))
    print("avg", sum(data2[i]) / len(data2[i]))

print("-" * 30)

for i in range(len(data2)):
    print(f"{i+1}번째 :", end = "")
    for j in range(len(data2[i])):
        print(f" [{j+1}]{data2[i][j]}", end = "")
    print()
    print("sum", sum(data2[i]))
    print("max", max(data2[i]))
    print("min", min(data2[i]))
    print("avg", sum(data2[i]) / len(data2[i]))

data3 = {
    "김인하" : [1, 2],
    "이인하" : [10, 20, 30, 40, 50, 60, 70],
    "송인하" : [11, 12, 13, 14],
    }

print("-" * 30)

for k in data3:
    print(k)

print("-" * 30)

for k in data3:
    print(data3[k])

print("-" * 30)

for k in data3:
    print(f"{k}:{data3[k]}")

print("-" * 30)

for k in data3:
    print(f"{k}: ", end = "")
    for v in range(len(data3[k])):
        print(f"[{v+1}]{data3[k][v]}", end = "")
    print()
    print("sum", sum(data3[k]))
    print("max", max(data3[k]))
    print("min", min(data3[k]))
    print("avg", sum(data3[k]) / len(data3[k]))





















