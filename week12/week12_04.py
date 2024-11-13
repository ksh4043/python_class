# week12_04.py

# C언어의 include와 유사
# from, import 키워드로 해당 파일의 메소드 직접 호출 가능
# from week12_02 import add
# from week12_02 import sub

from week12_02 import add,sub

# 다른 파일에 같은 메소드가 있을 경우 구별이 불가하기 때문에 마지막에 import된 파일만 사용
# from week12_02 import *   # 비추천

print(add(1,2)) # 호출
print(sub(1,2)) # 호출
