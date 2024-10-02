# week06_02.py

students = []
titles = ['국어', '영어', '수학']

number = int(input("인원 : "))
for n in range(number):
    print(f"{n+1} 학생>>")
    scores = []
    for t in titles:
        score = float(input(f"{t} 과목 : "))
        scores.append(score)
    students.append(scores)

for value in enumerate(students):
    print(value)
    print(value[0], value[1])

for value1, value2 in enumerate(students):
    print(value1, value2)

for value1, value2 in enumerate(students):
    print(value1, value2)
    for j, score in enumerate(value2):
        print(f"{titles[j]}:{score}")
