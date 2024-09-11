# week03_07.py

print(len("a"))
print(len([1,2]))
print(len((1,2,3)))

#"a".len()
#count("a")
"a".count("a")
#(1).count("a")

print("*" * 10)

test = "i am a BOY."
print(test.count("a"))
print(test.count("A"))

print(test.find("a"))
print(test.find("q"))
print(test.find("am"))
print(test.find("qm"))

print(test.index("a"))
#print(test.index("q"))
print(test.index("am"))
if "qm" in test:
    print(test.index("qm"))
else:
    print("There is no qm")

print(test.upper())
print(test.lower())
print(test.title())
print(test.capitalize())
print("/".join(test))

test = "    JMT University    "
print("|" + test.strip() + "|")
print("|" + test.lstrip() + "|")
print("|" + test.rstrip() + "|")

print(test.replace("University", "High School"))
print(test)

print(test.split())#리스트로 반환
print(test.split("i"))#리스트로 반

#%를 print 할 때는 %%
a = "%d%%" % 10
print(a)
