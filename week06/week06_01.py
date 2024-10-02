#week 05_01.py

values = [1,2,3,4]
new_values = []

for value in values:
    new_values.append(value * 3)

values_1_1 = [value for value in values]
print(values_1_1)

values_1_2 = [value * 3 for value in values]
print(values_1_2)
    
new_values2 = []
for value in values:
    if value % 2 == 0:
        new_values2.append(value * 3)

values_2_1 = [value * 3 for value in values if value % 2 == 0]
print(values_2_1)

print(values)
print(new_values)
print(new_values2)

values = ['1', '2', '3']

values_int = [int(value) for value in values]
print(values_int, type(values_int[0]))

mx = int(input("최대수 : "))
results = [v for v in range(1, mx + 1)]
