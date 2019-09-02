from datetime import datetime

class MyDate(datetime):
     def __format__(self, spec_str):
         if not spec_str:
             spec_str = '%Y-%m-%d %H:%M:%S'
         return self.strftime(spec_str)


class DateRange(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __contains__(self, needle):
        return self.start <= needle <= self.end

if __name__== "__main__":
    dr = DateRange(MyDate(2015, 1, 1), MyDate(2015, 12, 31))
    print( MyDate(2015, 4, 21) in dr )
    print( MyDate(2012, 4, 21) in dr )