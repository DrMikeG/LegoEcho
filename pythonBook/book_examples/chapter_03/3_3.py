
def zipEx():
    z = zip(['a', 'b', 'c', 'd'], ['x', 'y', 'z'])
    print next(iter(z))
    #('a', 'x')
    print next(iter(z))
    #('b', 'y')
    print next(iter(z))
    #('c', 'z')
    print next(iter(z))
    #Traceback (most recent call last):
    #File "<stdin>", line 1, in <module>
    #StopIteration

def mapEX():
    m = map(lambda x, y: max([x, y]), [4, 1, 7], [3, 4, 5])
    print next(m)
    #4
    print next(m)
    #4
    print next(m)
    #7
    print next(m)
    #Traceback (most recent call last):
    #  File "<stdin>", line 1, in <module>
    #StopIteration

def openEX():
    f = open('lines.txt')
    print next(f)
    #'line 1\n'
    print next(f)
    #'line 2\n'
    print next(f)
    #'line 5\n'
    print next(f)
    #Traceback (most recent call last):
    # File "<stdin>", line 1, in <module>
    #StopIteration

    print next(f)
    #Traceback (most recent call last):
    #File "<stdin>", line 1, in <module>
    #StopIteration
    f.readline()
    #''

def iterEx():
    dictionary = {'foo': 'bar', 'baz': 'bacon'}
    iterator = iter(dictionary.items())
    print next(iterator)
    #('foo', 'bar')
    print next(iterator)

    dictionary2 = {'foo': 'bar', 'baz': 'bacon'}
    iterator = iter(dictionary2.items())
    print next(iterator)
    #('foo', 'bar')
    dictionary2['spam'] = 'eggs'
    print next(iterator)
    #print next(iterator)
    #Traceback (most recent call last):
    #File "<stdin>", line 1, in <module>
    #RuntimeError: dictionary changed size during iteration

if __name__== "__main__":

#    zipEx()
    mapEX()
#    openEX()
    