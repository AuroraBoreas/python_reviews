# protocal view of python: data model method

# start with rough
class Polynomial:
    pass

p1 = Polynomial()
p2 = Polynomial()

p1.coeffs = 1, 2, 3
p2.coeffs = 3, 4, 3

# refine it
class Polynomial2:
    def __init__(self, *coeffs) -> None:
        self.coeffs = coeffs

    def __repr__(self):
        return 'Polynomial(*{!r})'.format(self.coeffs)

    def __add__(self, other):
        return Polynomial2(*(x + y for x, y in zip(self.coeffs, other.coeffs)))

    def __len__(self):
        return len(self.coeffs)

    def __call__(self):
        pass

p1 = Polynomial2(1,2,3)
p2 = Polynomial2(3,4,3)

