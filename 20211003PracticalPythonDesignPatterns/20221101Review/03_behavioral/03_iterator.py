"#" 
from __future__ import annotations
from collections.abc import Iterator, Iterable
from typing import Any, List


class AlphabeticIterator(Iterator):
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
    def __init__(self, word:List) -> None:
        self._word = word
    
    def __iter__(self) -> AlphabeticIterator:
        return AlphabeticIterator(self._word)

    def reverse(self) -> AlphabeticIterator:
        return AlphabeticIterator(self._word, True)

def client_code() -> None:
    w = WordIterable("hello world!")
    for c in w.reverse():
        print(c, end=' ')

if __name__ == '__main__':
    client_code()