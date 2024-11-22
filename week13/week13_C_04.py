# week13_C_04.py

# id: 202444091
# name: kim si hyeon

import datetime

books = []
parsingFormat = "%Y-%m-%d %H:%M:%S"

while True:
    number = input("도서번호: ").strip()
    if number == "":
        break
    intime =  datetime.strptime(input("대출시간: "), parsingFormat)
    outtime = datetime.strptime(input("반납시간: "), parsingFormat)

    book = {'num': number, 'in': intime, 'out': outtime}
    books.append(book)

 
for book in books:
    print(book['num'], book['in'], book['out'])
