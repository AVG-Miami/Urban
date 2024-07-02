class EvenNumbers:
    def __init__(self, start=0, end=1):
        self.start = start
        self.end = end
        self.i = start

    def __iter__(self):
        self.i = self.start - 1
        return self

    def __next__(self):
        self.i += 1
        if self.i > self.end:
            raise StopIteration()
        if not self.i % 2:
            return self.i
        else:
            print( '   ', self.i )


en = EvenNumbers( 10, 25 )
for i in en:
    print( i )
