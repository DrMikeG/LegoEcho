class BubbleExceptions(object):
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_instance, traceback):
        if exc_instance:
            print('Bubbling up exception: %s.' % exc_instance)
        return False

if __name__== "__main__":
#    with BubbleExceptions():
#        5 + 5

    with BubbleExceptions():
        5 / 0