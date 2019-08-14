
class ContextManager():
    def __init__(self):
        self.entered = False

    def __enter__(self):
        self.entered = True
        return self

    def __exit__(self, exc_type, exc_instance, traceback):
        self.entered = False


if __name__== "__main__":     
    cm = ContextManager()
    print cm.entered

    with cm:
        print cm.entered

    print cm.entered