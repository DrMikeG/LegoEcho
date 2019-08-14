
def squares(cursor=1):
    while True:
        response = yield cursor ** 2
        if response:
            cursor = int(response)
        else:
            cursor += 1

if __name__== "__main__":

    sq = squares()
    print next(sq)
    print next(sq)
    print sq.send(7)
    print next(sq)