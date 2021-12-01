# 
from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import Any


class AlphabeticIterator(Iterator):
    _position:int = None
    _reverse:bool = False

    def __init__(self, col:WordsIterable, reverse:bool=False) -> None:
        self._col     = col
        self._reverse = reverse
        self._position= -1 if reverse else 0

    def __next__(self) -> Any:
        try:
            rv = self._col[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()
        return rv

class WordsIterable(Iterable):
    def __init__(self) -> None:
        super().__init__()

    def __iter__(self) -> AlphabeticIterator:
        return super().__iter__()

    def get_reversed_col(self)->AlphabeticIterator:
        pass