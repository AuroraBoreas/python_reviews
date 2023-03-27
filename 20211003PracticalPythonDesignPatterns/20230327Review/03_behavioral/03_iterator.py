# 
from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import Any, Sequence

class AlphabeticIterator(Iterator):
    reverse: bool = False
    position: int = None

    def __init__(self, wi: WorldIterable, reverse: bool=False) -> None:
        self._wi = wi
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self) -> Any:
        try:
            res = self._wi[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration
        return res
    
class WorldIterable(Iterable):
    def __init__(self, seq: Sequence) -> None:
        self._seq = seq
    
    def __iter__(self) -> AlphabeticIterator:
        return AlphabeticIterator(self._seq)

    def reverse(self) -> AlphabeticIterator:
        return AlphabeticIterator(self._seq, True)