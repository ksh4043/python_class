# week13_C_11_2.py

# id:202444091
# name:kim si hyeon
# TimeStamp를 이용해서 대출/반납 시간을 만들어서 관리한다.

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

    members = os.listdir(mypath)
    for member in members:
        member_fullname = os.path.join(mypath, member)
        if os.path.isfile(member_fullname):
            # 111.txt -> 111 도서번호 -> 111 , .txt
            file_ext = os.path.splitext(member) # 확장자명과 파일명을 분리
            if file_ext and len(file_ext) == 2 and file_ext[-1] == "txt":
                number = file_ext[0].strip()
                books[number] = []
                with open(member_fullname, "r", encoding = "UTF-8") as f:
                    for line in f:
                        split_datas = line.strip().split("|")
                        if split_datas and len(split_datas) == 2:
                            intime = dt.strptime(split_datas[0], str_fmt)
                            if split_datas[1].strip():
                                outtime = dt.strptime(split_datas[1], str_fmt)
                            else:
                                outtime = None

                            books[number].append({"in":intime, "out":outtime})

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



