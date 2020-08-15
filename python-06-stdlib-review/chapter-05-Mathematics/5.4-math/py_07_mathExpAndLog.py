import sys, math
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def math_pow():
    INPUTS = [
        # Typical uses
        (2, 3),
        (2.1, 3.2),
        # Always 1
        (1.0, 5),
        (2.0, 0),
        # Not a number
        (2, float('nan')),
        # Roots
        (9.0, 0.5),
        (27.0, 1.0 / 3),
    ]
    for x, y in INPUTS:
        print('{:5.1f} ** {:5.3f} = {:6.3f}'.format(x, y, math.pow(x, y)))

### TODOS: P316

if __name__ == "__main__":
    # power
    math_pow()