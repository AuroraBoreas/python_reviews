# iterator
from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import List, Any

class AlphabeticIterator(Iterator):
    _position:int = None
    _reverse:bool = False
    
    def __init__(self, col:WordsIterable, reverse:bool=False)->None:
        self._col      = col
        self._reverse  = reverse
        self._position = -1 if reverse else 0

    def __next__(self)->Any:
        try:
            val = self._col[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()
        return val

class WordsIterable(Iterable):
    def __init__(self, col:List[Any]=[]) -> None:
        self.words:List[str] = col

    def add(self, word:str)->None:
        self.words.append(word)

    def __iter__(self)->AlphabeticIterator:
        return AlphabeticIterator(self.words)

    def reverse(self)->AlphabeticIterator:
        return AlphabeticIterator(self.words, True)
