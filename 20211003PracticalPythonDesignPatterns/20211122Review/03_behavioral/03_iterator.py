# 
from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import Any, List, TypeVar
_T_co = TypeVar('_T_co')

class AlphabeticIterator(Iterator):
    _position:int = None
    _reverse:bool = False

    def __init__(self, col:WordsIterable, reverse:bool=False) -> None:
        self._col      = col
        self._reverse  = reverse
        self._position =  -1 if reverse else 0

    def __next__(self) -> _T_co:
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

    def get_reversed_col(self)->AlphabeticIterator:
        return AlphabeticIterator(self._col, True)