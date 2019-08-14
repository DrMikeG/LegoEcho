class MyClass(object):
    def __init__(self):
        print('The _init_ method is running.')
 
    def __eq__(self, other):
        # All instances of MyClass are equivalent to one another, and they
        # are not equivalent to instances of other classes.
        return type(self) == type(other)


if __name__== "__main__":
    mc = MyClass()

    print MyClass() == MyClass()
    print MyClass() == 42