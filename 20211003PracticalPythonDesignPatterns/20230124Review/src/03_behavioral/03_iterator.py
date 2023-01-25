from __future__ import annotations
from collections.abc import Iterable, Iterator
from dataclasses import dataclass
from typing import Any, Sequence

@dataclass
class AlphabeticIterator(Iterator):
    position: int
    reverse: bool

    def __init__(self, s: WordsIterable, reverse: bool=False) -> None:
        self._s       = s
        self.reverse  = reverse
        self.position = -1 if reverse else 0

    def __next__(self) -> Any:
        try:
            res: Any = self._s[self.position]
            self.position += -1 if self.reverse else 1
        except IndexError:
            raise StopIteration
        return res

class WordsIterable(Iterable):
    def __init__(self, seq: Sequence) -> None:
        self._seq = seq

    def __iter__(self) -> AlphabeticIterator:
        return AlphabeticIterator(self._seq)

    def reverse(self) -> AlphabeticIterator:
        return AlphabeticIterator(self._seq, True)
