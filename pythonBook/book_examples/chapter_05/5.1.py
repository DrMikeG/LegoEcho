from datetime import datetime

class Animal(object):
    """A class representing an arbitrary animal."""

    def __init__(self, name):
        self.name = name

    def eat(self):
        pass

    def go_to_vet(self):
        pass


class Cat(Animal):
    def meow(self):
        pass

    def purr(self):
        pass

if __name__== "__main__":
    dr = DateRange(MyDate(2015, 1, 1), MyDate(2015, 12, 31))
    print( MyDate(2015, 4, 21) in dr )
    print( MyDate(2012, 4, 21) in dr )