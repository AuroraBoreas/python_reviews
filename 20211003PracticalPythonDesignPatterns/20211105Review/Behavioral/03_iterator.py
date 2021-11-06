# iterator
from __future__ import annotations
from typing import Iterable, Iterator, List, Any


class AlphabeticalOrderIterator(Iterator):
    _position:int = None
    _reverse:bool = False

    def __init__(self, collection:WordsCollection, reverse:bool=False) -> None:
        self._collection = collection
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self)->Any:
        try:
            val = self._collection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()
        return val

class WordsCollection(Iterable):
    def __init__(self, collection:List[Any]=[]) -> None:
        self._collection = collection

    def __iter__(self)->AlphabeticalOrderIterator:
        return AlphabeticalOrderIterator(self._collection)

    def get_reverse_iterator(self)->AlphabeticalOrderIterator:
        return AlphabeticalOrderIterator(self._collection, True)

    def add_item(self, item:Any)->None:
        self._collection.append(item)

def client_code()->None:
    col = WordsCollection()
    col.add_item('first')
    col.add_item('second')
    col.add_item('third')

    print('straight traversal:')
    print('\n'.join(col))
    print()

    print('reverse traversal:')
    print('\n'.join(col.get_reverse_iterator()), end='')

if __name__ == '__main__':
    client_code()