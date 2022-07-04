"Python is a protocoal orientated lang; every top-level function has a corresponding dunder method implemented;" 
from __future__ import annotations
from collections.abc import Iterable, Iterator
from http import client
from typing import Any, List

class AlphabeticIterator(Iterator):
    _position:int = None
    _reverse:bool = False

    def __init__(self, col:WordsIterable, reverse:bool=False) -> None:
        self._col      = col
        self._reverse  = reverse
        self._position = -1 if reverse else 0

    def __next__(self) -> Any:
        try:
            rv = self._col[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()
        return rv

class WordsIterable(Iterable):
    def __init__(self, col:List[Any]) -> None:
        self._col = col

    def __iter__(self) -> AlphabeticIterator:
        return AlphabeticIterator(self._col)

    def reverse(self) -> AlphabeticIterator:
        return AlphabeticIterator(self._col, True)

def client_code(words:List[Any]) -> None:
    wi = WordsIterable(words)
    for i in wi:
        print(i, end=' ')
    print()
    for i in wi.reverse():
        print(i, end=' ')

if __name__ == '__main__':
    client_code("hello world!")