# week12_08.py

PI = 3.141592


class Math:
    def solv(self, r):
        return PI * (r**2)


def add(a,b):
    return a + b


# __name__ 변수가 __main__ 이라는 것은 실행하는 파일이 해당 파일(main파일)이라는 의미
if __name__ == "__main__":
    print(add(1,2))
