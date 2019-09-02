class Timespan(object):
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __len__(self):
        return (self.hours * 3600) + (self.minutes * 60) + self.seconds

    def __repr__(self):
        return 'Timespan(hours=%d, minutes=%d, seconds=%d)' % \
               (self.hours, self.minutes, self.seconds)

if __name__== "__main__":
    ts = Timespan(hours=2, minutes=30, seconds=1)
    print len(ts)

    print Timespan()
    print Timespan(hours=2, minutes=30)