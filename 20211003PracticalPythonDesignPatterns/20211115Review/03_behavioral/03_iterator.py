# iterator 
from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import List, TypeVar, Any
_T_co = TypeVar('_T_co')

class AlphabeticIterator(Iterator):
    _position:int = None
    _reverse:bool = False

    def __init__(self, col:WordsIterable, reverse:bool=False) -> None:
        self.col = col
        self._reverse = reverse
        self._position = -1 if reverse else 0
        
    def __next__(self) -> _T_co:
        try:
            rv = self.col[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()
        return rv

class WordsIterable(Iterable):
    def __init__(self, col:List[Any]) -> None:
        self.col = col

    def __iter__(self) -> AlphabeticIterator[_T_co]:
        return AlphabeticIterator(self.col)

    def get_reverse_collection(self)->AlphabeticIterator[_T_co]:
        return AlphabeticIterator(self.col, True)

    def add(self, item:Any)->None:
        self.col.append(item)

    def __str__(self)->str:
        return '{}'.format(', '.join(map(str, self.col)), end='')

def client_code()->None:
    w = WordsIterable(['cy', 'zl'])
    print(f'{w.get_reverse_collection()}')