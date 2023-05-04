"Python is a protocol orientated language; every top-level function implements its dunder method;" 

from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import Any, Sequence

class AlphabeticIterator(Iterator):
    position: int = None
    reverse: bool = None
    
    def __init__(self, wi: WordIterable, reverse: bool=False) -> None:
        self._wi = wi
        self.reverse = reverse
        self.position = -1 if reverse else 0

    def __next__(self) -> Any:
        try:
            res = self._wi[self.position]
            self.position += -1 if self.reverse else 1
        except IndexError:
            raise StopIteration
        return res
    
class WordIterable(Iterable):
    def __init__(self, seq: Sequence) -> None:
        self._seq = seq

    def __iter__(self) -> AlphabeticIterator:
        return AlphabeticIterator(self._seq)
    
    def reverse(self) -> AlphabeticIterator:
        return AlphabeticIterator(self._seq, True)
    
def client_code() -> None:
    wi: WordIterable = WordIterable("hello world!")
    for i in wi:
        print(i, end=' ')
    print()
    for i in wi.reverse():
        print(i, end=' ')

def main() -> None:
    client_code()

if __name__ == '__main__':
    main()