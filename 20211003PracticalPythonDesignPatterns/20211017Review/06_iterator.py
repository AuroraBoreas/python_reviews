# navigate

class Compute:
    def __init__(self, last:int)->None:
        self.last = last
        self.first = 0

    def __iter__(self):
        return self

    def __next__(self):
        rv = self.first
        self.first += 1
        if self.first >= self.last:
            raise StopIteration()
        return rv
