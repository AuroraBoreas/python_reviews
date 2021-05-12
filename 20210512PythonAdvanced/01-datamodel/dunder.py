"#Python is a protocol orientated lang; every top-level function has a corresponding dunder method implemented;" 

class Polynormial:
    def __init__(self, *args):
        self.args = args
    
    def __repr__(self):
        return "Polynormial{!r}".format(self.args)

    def __add__(self, other):
        return Polynormial(*(x + y for x, y in zip(self.args, other.args)))

    def __sub__(self, other):
        return Polynormial(*(x - y for x, y in zip(self.args, other.args)))

    def __call__(self):
        pass

if __name__ == "__main__":
    p1: Polynormial = Polynormial(1, 2, 3)
    p2: Polynormial = Polynormial(1, 2, 3)
    print(p1 + p2)