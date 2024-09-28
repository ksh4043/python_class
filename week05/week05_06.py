# week05_06.py
'''
name = ""
while name != "오창룡":
    name = input('이름:')
    print(name)


name = ""
while name != 'oh':
    name = input("이름:").strip().lower()
    print(name)

flag = True
while flag:
    name = input("이름:").strip().lower()
    if name == "oh":
        flag = False
    print(name)
'''

while True:
    name = input("이름:").strip().lower()
    
    if name == "oh":
        break
    elif name != "오":
        print(name)
    
