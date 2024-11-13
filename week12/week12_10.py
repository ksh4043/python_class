# week12_10.py

def test():
    raise NotImplementedError("test함수 미작성")   # throw new Exception과 동일

while True:
    try:
        dvd = int(input("피제수:"))
        dvs = int(input("제수:"))
        result = dvd / dvs
        print(result)
        test()
    except ValueError:
        print("정수 데이터만 입력")
    except ZeroDivisionError:
        print("ZeroDivisionError!")
    except Exception as e:
        print(e)
    else:
        print("try문이 완벽히 실행하면 할 것")
    finally:
        print("안녕히 계세요 여러분")
        break
    #except:
    #    print("예외 발생. 죽음.")
    #    break

