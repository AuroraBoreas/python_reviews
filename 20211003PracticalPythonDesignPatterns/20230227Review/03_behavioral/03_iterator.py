# 
from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import Any, Sequence

class AlphabeticIterator(Iterator):
    position: int = None
    reverse: bool = None

    def __init__(self, wi: WorldIterable, reverse: bool=False) -> None:
        self._wi      = wi
        self.reverse  = reverse
        self.position = -1 if reverse else 0

    def __next__(self) -> Any:
        try:
            res = self._wi[self.position]
            self.position += -1 if self.reverse else 1
        except IndexError:
            raise StopIteration
        return res

class WorldIterable(Iterable):
    def __init__(self, words: Sequence) -> None:
        self._words = words

    def __iter__(self) -> AlphabeticIterator:
        return AlphabeticIterator(self._words)

    def reverse(self) -> AlphabeticIterator:
        return AlphabeticIterator(self._words, True)

def client_code() -> None:
    w: WorldIterable = WorldIterable("hello world!")
    for c in w:
        print(c, end=' ')
    print()
    for c in w.reverse():
        print(c, end=' ')

def main() -> None:
    client_code()

if __name__ == '__main__':
    main()