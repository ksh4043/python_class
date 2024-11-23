# book.py

# id: 202444091
# name: kim si hyeon

from datetime import datetime as dt

class Book1:
    def __init__(self, number, inTime, outTime):
        self.number = number
        self.inTime = inTime
        self.outTime = outTime


    def diff_seconds(self, inTime, outTime):
        if outTime == None:
            outTime = dt.now()

        return (outTime - inTime).total_seconds()


    def __str__(self):
        return f"{self.number} {self.inTime} {self.outTime}"
