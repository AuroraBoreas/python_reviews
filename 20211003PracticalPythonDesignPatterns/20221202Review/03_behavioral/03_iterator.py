"#" 

from typing import Any, List
from collections.abc import Iterable, Iterator

class AlphabeticIterator(Iterator):
    _reverse: bool = None
    _position: int = None

    def __init__(self, word:List[Any], reverse:bool=False) -> None:
        self._word     = word
        self._reverse  = reverse
        self._position = -1 if reverse else 0
        
    def __next__(self) -> Any:
        try:
            res = self._word[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()
        return res

class WordIterable(Iterable):
    def __init__(self, seq:List) -> None:
        self._seq = seq

    def __iter__(self) -> AlphabeticIterator:
        return AlphabeticIterator(self._seq)

    def reverse(self) -> AlphabeticIterator:
        return AlphabeticIterator(self._seq, True)

def client_code() -> None:
    w1 = WordIterable("hello world!")
    for i in w1:
        print(i, end=' ')
    print()
    for i in w1.reverse():
        print(i, end=' ')

if __name__ == '__main__':
    client_code()