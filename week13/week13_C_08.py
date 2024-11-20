# week13_C_08.py

# id: 202444099
# name: park soi

import datetime
import os
from datetime import datetime as dt

mypath = "c:\\book1_202444099"
myfile = "list.txt"
fullfile = os.path.join(mypath, myfile)


if __main__ == "__name__":
    if not os.path.isdir(mypath):
        os.mkdir(mypath)
    
    books = []
    parsingFormat = "%Y-%m-%d %H:%M:%S"

    def diff_seconds(d1, d2):
        if d2 == None:
            d2 = dt.now()
        return (d2 - d1).total_seconds()

    while True:
        number = input("도서번호: ").strip()
        if number == "":
            break

        while True:
            try:
                intime = input("대출시간: ").strip()
                if intime:
                    intime = dt.strptime(intime, parsingFormat)
                    break
            except:
                pass

        while True:
            try:
                outtime = input("반납시간: ").strip()
                if not outtime:
                    outtime = None
                else:
                    outtime = dt.strptime(outtime, parsingFormat)
                break
            except:
                pass
        

        book = {'num': number, 'in': intime, 'out': outtime}
        books.append(book)

     
    for book in books:
        print(book['num'], book['in'], book['out'])
        print(diff_seconds(book['in'], book['out']))
