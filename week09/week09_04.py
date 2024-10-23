# week09_04.py

# set자료형; 중복된 데이터 제거
s1 = {1, 2, 3, 3, 4}
s2 = {'a', 'b', '1', 1, '1'}

print(s1)
print(s2)

print(s1 & s2)  # 교집합 조건.
print(s1 | s2)  # 합집합
print(s1 - s2)  # 차집합

s1.add('6')
print(s1)
s1.update([1,2,3,7])    # 대량의 데이터를 추가
print(s1)
s1.remove(3)
print(s1)
