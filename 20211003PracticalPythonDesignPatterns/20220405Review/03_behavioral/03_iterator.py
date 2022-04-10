"#" 

from collections.abc import Iterable, Iterator
from typing import Any, List

class AlphabeticIterator(Iterator):
    _position:int = None
    _reverse:bool = False

    def __init__(self, words:List[str], reverse:bool=False) -> None:
        self._words    = words
        self._reverse  = reverse
        self._position = -1 if self._reverse else 0

    def __next__(self) -> Any:
        try:
            rv = self._words[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()
        return rv

class WordsIterable(Iterable):
    def __init__(self, words:List[str]) -> None:
        self._words = words

    def __iter__(self) -> AlphabeticIterator:
        return AlphabeticIterator(self._words)

    def reverse(self) -> AlphabeticIterator:
        return AlphabeticIterator(self._words, True)