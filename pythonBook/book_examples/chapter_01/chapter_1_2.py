import functools


def requires_ints(decorated):
    @functools.wraps(decorated)
    def inner(*args, **kwargs):
        # Get any values that may have been sent as keyword arguments.
        kwarg_values = [i for i in kwargs.values()]

        # Iterate over every value sent to the decorated method, and
        # ensure that each one is an integer; raise TypeError if not.
        for arg in list(args) + kwarg_values:
            if not isinstance(arg, int):
                raise TypeError('%s only accepts integers as arguments.' %
                                decorated.__name__)

        # Run the decorated method, and return the result.
        return decorated(*args, **kwargs)
    return inner

@requires_ints
def foo(x, y):
    """Return the sum of x and y."""
    return x + y


if __name__== "__main__":     
    help(foo)
    print foo(1,2)