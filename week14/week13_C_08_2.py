# week13_B_08_2.py

# id:202444091
# name:kim si hyeon

from datetime import datetime as dt
import os

str_fmt = "%Y-%m-%d %H:%M:%S"


def diff_seconds(intime, outtime):
    if not outtime:
        outtime = dt.now()
    return (outtime - intime).total_seconds()


if __name__ == "__main__":
    mydir = "c:\\book2_202444091"

    if not os.path.isdir(mydir):
        os.mkdir(mydir)

    books = {}

    # read 작업해야 할 곳!
    # 파일이 있는지 확인
    # 있으면 파싱, 없으면 그대로 밑으로 떨어지면 됨.

    while True:
        number = input("도서번호:").strip()
        if not number:
            break

        if not number in books.keys():
            books[number] = []
        else:
            for time in books[number]:
                if time['out'] == None:
                    print("아직 반납이 안된 책")
                    continue

        while True:
            try:
                intime = input("대여시간:").strip()
                if intime:
                    intime = dt.strptime(intime, dtformat)
                    break
            except:
                pass

        while True:
            try:
                outtime = input("반납시간:").strip()
                if not outtime:
                    outtime = None
                    break
                outtime = dt.strptime(outtime, dtformat)
                break
            except:
                pass

        #books = {"num": number, "in": intime, "out": outtime}
        #books.append(book)

        times = {"in": intime, "out": outtime}
        books[number].append(times)

        book_fullname = os.path.join(mypath, number + ".txt")
        with open(book_fullname, "a",, encoding = "UTF-8") as f:
            intime = dt.strftime(intime, str_fmt)
            if outtime:
                outtime = dt.strftime(outtime, str_fmt)
                f.write(f"{intime}|{outtime}\n")
            else:
                f.write(f"{intime}|")

    for number, times in books.items():
        print("도서번호 :",number)
        for time in times:
            print(time["in"], time["out"])
            print(diff_seconds(time["in"], time["out"]))



