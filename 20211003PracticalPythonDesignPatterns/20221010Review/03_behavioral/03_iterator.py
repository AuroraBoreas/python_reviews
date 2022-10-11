#
from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import Any, List

class WordIterator(Iterator):
    _position:int = None
    _reverse:bool = None
    def __init__(self, s:WordIterable, reverse:bool=False) -> None:
        self._s        = s
        self._reverse  = reverse
        self._position = -1 if reverse else 0

    def __next__(self) -> Any:
        try:
            res = self._s[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()
        return res

class WordIterable(Iterable):
    def __init__(self, words:List[Any]) -> None:
        self._words = words

    def __iter__(self) -> WordIterator:
        return WordIterator(self._words)

    def reverse(self) -> WordIterator:
        return WordIterator(self._words, True)

def client_code() -> None:
    w = WordIterable("helllo world")
    [print(i, sep='', end=' ') for i in w.reverse()]

if __name__ == '__main__':
    client_code()