# week13_C_03.py

# id: 202444099
# name: park soi

import datetime 

books = []

while True:
    number = input("도서번호: ").strip()
    if number == "": # if not number:
        break
    intime =  input("대출시간: ")
    outtime = input("반납시간: ")

    book = {'num': number, 'in': intime, 'out': outtime}
    books.append(book)
    
    #library = {}
    #library['num'] = number
    #library['in'] = intime
    #library['out'] = outtime

for book in books:
    print(book['num'], book['in'], book['out'])
