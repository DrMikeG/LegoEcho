import random

class MyClass(object):
    def __init__(self):
        print('The _init_ method is running.')
 
    def __eq__(self, other):
        # All instances of MyClass are equivalent to one another, and they
        # are not equivalent to instances of other classes.
        return type(self) == type(other)

class Dice(object):
    """A class representing a dice with an arbitrary number
    of sides.
    """
    def __init__(self, sides=6):
        self._sides = sides

    def roll(self):
        return random.randint(1, self._sides)

class MyClass2(object):
    def __new__(cls):
        instance = super(MyClass2, cls).__new__(cls)
        print '[do work on instance]'
        return instance

class Xon(object):
    def __del__(self):
        print('AUUUUUUGGGGGGHH!')

if __name__== "__main__":
    mc = MyClass()

    print MyClass() == MyClass()
    print MyClass() == 42

    die = Dice(sides=20)
    print die._sides
    print die.roll()
    print die.roll()

    print MyClass2()

    print Xon()
    'foo'
