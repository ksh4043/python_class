# week10_03.py

myfile = "c:\\s202444091\\ksh_02.txt"

f = open(myfile, 'r')

# type1
# d = f.read()  파일 전체 읽기
# print(d)

# type2
#while True:
#    d = f.readline()    # 한줄씩 읽기
#    if not d:
#        break
#    print(d.strip())

# type3
d = f.readlines()   # 라인 별로 리스트에 넣어서 반환
for line in d:
    print(line.strip())

#readline, readlines >> 공백문자열,\n까지 읽어들임

f.close()
