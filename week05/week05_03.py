# week05_03.py

socnum = input("주민등록번호")


index = 6
if "-" in socnum:
    index = 7

gender = int(socnum[index]) % 2

if gender == 0:
    msg = "여성"
else:
    msg = "남성"

print(f"성별 : {msg}")
