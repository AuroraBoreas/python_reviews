# iterator

class Compute:
    def __init__(self, last:int)->int:
        self.last = last
        self.first = 0

    def __iter__(self):
        return self

    def __next__(self):
        rv = self.first
        self.first += 1
        if self.first > self.last:
            raise StopIteration()
        return rv

if __name__ == '__main__':
    for i in Compute(10):
        print(i)
