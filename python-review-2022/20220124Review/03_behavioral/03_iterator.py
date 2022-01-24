# 
from __future__ import annotations
from collections.abc import Any, Iterable, Iterator
from typing import List

class AlphabeticIterable(Iterable):
    _position:int = None
    _reverse:bool = False

    def __init__(self, col:WordsIterator, reverse:bool=False) -> None:
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

class WordsIterator(Iterator):
    def __init__(self, col:List) -> None:
        self._col = col

    def __iter__(self) -> AlphabeticIterable:
        return AlphabeticIterable(self._col)

    def reverse(self)->AlphabeticIterable:
        return AlphabeticIterable(self._col, True)