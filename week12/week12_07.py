# week12_07.py

import week12_06 as m
from week12_06 import PI # 같은 파일의 변수나 메소드를 단독으로 사용하고 싶으면 form, import
from week12_06 import PI as pi

print(m.PI) # 변수도 사용 가능함
print(PI)
print(pi)
print(m.add(m.PI, 4.4))
obj = m.Math()
print(obj.solv(2))
