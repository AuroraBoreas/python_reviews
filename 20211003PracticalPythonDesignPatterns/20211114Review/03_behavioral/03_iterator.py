# iterator
from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import Any, List

class AlphabeticIterator(Iterator):
    _position:int = None
    _reverse:bool = False
    
    def __init__(self, col:WordsIterable, reverse:bool=False) -> None:
        self.col       = col
        self._reverse  = reverse
        self._position = -1 if reverse else 0
    
    def __next__(self) -> Any:
        try:
            rv = self.col[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()
        return rv

class WordsIterable(Iterable):
    def __init__(self, col:List[Any]=None)->None:
        self.col = col

    def add(self, item:Any)->None:
        self.col.append(item)

    def get_reverse_iterator(self)->AlphabeticIterator:
        return AlphabeticIterator(self.col, True)

    def __iter__(self) -> AlphabeticIterator:
        return AlphabeticIterator(self.col)
    
    def __str__(self)->None:
        return '{}\n'.format(', '.join(map(str, self.col)), end='')

def client_code()->None:
    wi = WordsIterable(['zhangliang'])
    wi.add('cy')
    ai = wi.get_reverse_iterator()
    print(list(ai))

if __name__ == '__main__':
    client_code()