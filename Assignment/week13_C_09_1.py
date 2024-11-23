# week13_C_09_1.py

# id: 202444091
# name: kim si hyeon

import os
from datetime import datetime as dt

path = "c:\\book1_202444091"
file = "list.txt"
fullfile = os.path.join(path, file)

if __name__ == "__main__":
    if not os.path.isdir(path):
        os.mkdir(path)

    books = []
    parsingFormat = "%Y-%m-%d %H:%M:%S"

    def diff_seconds(d1, d2):
        if d2 == None:
            d2 = dt.now()
        return (d2 - d1).total_seconds()


    if not os.path.exists(fullfile):
        print(f"{fullfile}은 존재하지 않습니다.")
    else:
        with open(fullfile, "r") as readFile:
            infos = readFile.readlines()

            for info in infos:
                splitDatas = info.strip().split("|")
                r_num = splitDatas[0]
                r_inTime = dt.strptime(splitDatas[1], parsingFormat)
                r_outTime = dt.strptime(splitDatas[2], parsingFormat) if splitDatas[2] else None
                books.append({"num" : r_num, "in" : r_inTime, "out" : r_outTime})
                
        if books:
            print("복구한 정보입니다.")
            for book in books:
                print(f"{book['num']} {book['in']} {book['out']}")
        else:
            print("파일이 비어있습니다.")
                

    while True:
        number = input("도서번호 : ").strip()
        if number == "":
            break

        while True:
            try:
                inTime = input("대출시간 : ").strip()
                if inTime:
                    inTime = dt.strptime(inTime, parsingFormat)
                    break
            except:
                pass

        while True:
            try:
                outTime = input("반납시간 : ").strip()
                if outTime:
                    outTime = dt.strptime(outTime, parsingFormat)
                else:
                    outTime = None
                break
            except:
                pass

        books.append({"num" : number, "in" : inTime, "out" : outTime})

    for book in books:
        print(f"{book['num']} {book['in']} {book['out']}")
        print(diff_seconds(book['in'], book['out']))

    with open(fullfile, "w") as f:
        for book in books:
            if isinstance(book['out'], dt):
                b_outTime = dt.strftime(book['out'], parsingFormat) if book['out'] else ""
            if isinstance(book['in'], dt):
                b_inTime = dt.strftime(book['in'], parsingFormat)
            
            f.write(f"{book['num']}|{b_inTime}|{b_outTime}\n")
