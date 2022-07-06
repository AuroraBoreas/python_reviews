# 
from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import Any, List

class AlphabeticIterator(Iterator):
    _position:int = None
    _reverse:bool = False

    def __init__(self, col:WordIterable, reverse:bool=False) -> None:
        self._col      = col
        self._reverse  = reverse
        self._position = -1 if reverse else -1

    def __next__(self) -> Any:
        try:
            rv = self._col[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()
        return rv

class WordIterable(Iterable):
    def __init__(self, col:List) -> None:
        self._col = col

    def __iter__(self) -> AlphabeticIterator:
        return AlphabeticIterator(self._col)

    def reverse(self) -> AlphabeticIterator:
        return AlphabeticIterator(self._col, True)

def client_code() -> None:
    w = WordIterable("hello world!")
    for i in w:
        print(i, end=' ')
    print()
    for i in w.reverse():
        print(i, end=' ')

if __name__ == '__main__':
    client_code()