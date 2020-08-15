import sys, random
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def random_shuffle():
    import itertools
    FACE_CARDS = tuple('JQKA')
    SUITS      = tuple('HDCS')
    def new_deck():
        return [
            '{:>2}{}'.format(*c)
            for c in itertools.product(
                itertools.chain(range(2, 11), FACE_CARDS),
                SUITS,
            )
        ]
    pass

if __name__ == "__main__":
    random_shuffle()