"#" 
from __future__ import annotations

from collections.abc import Iterable, Iterator
from dataclasses import dataclass
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

from typing import TypeVar, Sequence
T = TypeVar('T')

@dataclass
class AlphabeticIterator(Iterator):
    _position: int
    _reverse: bool

    def __init__(self, worditerable: WordIterable, reverse: bool = False) -> None:
        self._wi: WordIterable = worditerable
        self._reverse          = reverse
        self._position         = -1 if reverse else 0

    def __next__(self) -> T:
        try:
            res: T = self._wi[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()
        return res

class WordIterable(Iterable):
    def __init__(self, seq: Sequence) -> None:
        self._seq: Sequence = seq

    def __iter__(self) -> AlphabeticIterator:
        return AlphabeticIterator(self._seq)

    def reverse(self) -> AlphabeticIterator:
        return AlphabeticIterator(self._seq, True)

def main() -> None:
    wi: WordIterable = WordIterable("hello world")
    logging.info(' '.join(i for i in wi))
    logging.info(' '.join(i for i in wi.reverse()))

if __name__ == '__main__':
    main()
