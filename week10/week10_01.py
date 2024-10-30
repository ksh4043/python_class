# week10_01.py

myfile = "c:\\s202444091\\ksh.txt"

# 1. 열기
# f = open(myfile, 'w')   # 쓰기모드 (덮어쓰기)
#f = open(myfile, 'a')   # 추가모드 (기존 파일이 없으면 새로 생성) 

# 2. 작업
#f.write("김시현\n")
#print(f.read())

# 3. 닫기
#f.close()

f = open(myfile, 'r')   # 읽기모드

print(f.read())

f.close()
