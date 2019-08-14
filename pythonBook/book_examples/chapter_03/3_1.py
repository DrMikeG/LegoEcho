def fibonacci():
    yield 1
    yield 1
    yield 2
    yield 3
    yield 5
    yield 8


def fibonacci_inf():
    numbers = []
    while True:
        if len(numbers) < 2:
            numbers.append(1)
        else:
            numbers.append(sum(numbers))
            numbers.pop(0)
        # yield final element of list
        yield numbers[-1] 
        continue

if __name__== "__main__":
    for i in fibonacci():
        print(i)

#    for i in fibonacci_inf():
#        print(i)

    # this does not run the generator code
    gen = fibonacci()
    print next(gen)