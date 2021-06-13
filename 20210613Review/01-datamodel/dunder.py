"#Python is a protocol orientated lang; every top-level function or syntax has a corresponding dunder method implemented;" 

class Polynomial:
    def __init__(self, *args):
        self._num = 69
        self.args = args

    def __repr__(self):
        return "Polynomial{!r}".format(self.args)

    def __add__(self, other):
        return Polynomial(*(x + y for x, y in zip(self.args, other.args)))

    def __call__(self):
        return 'U call I come'
    
    @classmethod
    def hello(cls, name: str)->str:
        return f"hello {name}"

    @staticmethod
    def say():
        return "say something"

    @property
    def price(self):
        return self._num

    @price.setter
    def price(self, val: int):
        self._num = val

    @price.getter
    def price(self):
        return self._num

    @price.deleter
    def price(self):
        del self._num

if __name__ == "__main__":
    p1: Polynomial = Polynomial(1, 2, 3)
    p2: Polynomial = Polynomial(1, 2, 3)
    print(p1 + p2)