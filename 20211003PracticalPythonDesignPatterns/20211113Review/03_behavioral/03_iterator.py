# iterator
from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import Any, List


class AlphabeticIterator(Iterator):
    _position:int = None
    _reverse:bool = False
    
    def __init__(self, col:WordsIterable, reverse:False) -> None:
        self.col = col
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self)->Any:
        try:
            rv = self.col[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()
        return rv

class WordsIterable(Iterable):
    def __init__(self, col:List[Any])->None:
        self.col = col

    def __iter__(self)->AlphabeticIterator:
        return AlphabeticIterator(self.col)
    
    def add(self, item:Any)->None:
        self.col.append(item)

    def get_reverse_iterator(self)->AlphabeticIterator:
        return AlphabeticIterator(self.col, True)

def client_code()->None:
    w = WordsIterable(list('zhang liang'))
    w.add('cy')
    a = w.get_reverse_iterator()
    print(list(a))

if __name__ == '__main__':
    client_code()