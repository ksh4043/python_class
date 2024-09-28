# week04_04.py
motorcycles = ["honda", "yamada", "suzuki"]
print(motorcycles)

#요소변경
motorcycles[0] = "bmw"
print(motorcycles)

#추가
motorcycles.append("vespa")
print(motorcycles)

#삽입
motorcycles.insert(0, "daelim")
print(motorcycles)

motorcycles.insert(10, "ducati")
print(motorcycles)

motorcycles = ["honda", "yamada", "suzuki",
               "bmw", "ducati", "vespa", "kia"]

del motorcycles[2]
print(motorcycles)

del motorcycles[-3]
print(motorcycles)

del motorcycles[:2]
print(motorcycles)

del motorcycles[:] #슬라이싱 전체
print(motorcycles)

# index out of range
#del motorcycles[10]
#print(motorcycles)

motorcycles = ["honda", "yamada", "suzuki",
               "bmw", "ducati", "vespa"]

popdata = motorcycles.pop()
print(motorcycles, popdata)

popdata = motorcycles.pop()
print(motorcycles, popdata)

popdata = motorcycles.pop(2)
print(motorcycles, popdata)

popdata = motorcycles.remove("yamada")
print(motorcycles, popdata)

target = "YAMADA"
if target in motorcycles:
    popdata = motorcycles.remove("YAMADA")
    print(motorcycles, popdata)
else:
    print(f"{target} 없음")

target = 20
if target < len(motorcycles):
    popdata = motorcycles.pop(20)
    print(motorcycles, popdata)
else:
    print(f"{target} 인덱스 사용 불가")
















