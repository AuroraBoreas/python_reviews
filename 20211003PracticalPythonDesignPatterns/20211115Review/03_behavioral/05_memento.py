# caretaker - [ originator - memento ] 
from __future__ import annotations
from abc import ABC, abstractmethod
import random
import string
import datetime
from typing import List

class Caretaker:
    _mementos:List[Memento] = []

    def __init__(self, originator:Originator) -> None:
        self._originator = originator

    def backup(self)->None:
        self._mementos.append(self._originator.save())

    def undo(self)->None:
        if not len(self._mementos):
            return
        memento = self._mementos.pop()
        try:
            self._originator.restore(memento)
        except Exception:
            self.undo()
        
    def show_history(self)->None:
        for memento in self._mementos:
            print(f'  {memento.get_name()}')

class Originator:
    def __init__(self, state:str) -> None:
        self._state = state

    def _generate_random_string(self, length:int=10)->None:
        self._state = ''.join(random.sample(string.ascii_letters, length))

    def save(self)->Memento:
        return Memento(self._state)

    def restore(self, memento:Memento)->None:
        self._state = memento.get_state()

    def operation(self)->None:
        self._generate_random_string(30)

class IMemento(ABC):    
    @abstractmethod
    def get_state(self)->str:
        pass

    @abstractmethod
    def get_date(self)->str:
        pass

    @abstractmethod
    def get_name(self)->str:
        pass

class Memento(IMemento):
    def __init__(self, state:str) -> None:
        self._state = state
        self._date  = str(datetime.datetime.now())[:19]

    def get_date(self) -> str:
        return self._date

    def get_state(self) -> str:
        return self._state
    
    def get_name(self) -> str:
        return f'({self._date}) / ({self._state[:9]})'

def client_code()->None:
    o = Originator('zhangliangcscy')
    c = Caretaker(o)

    c.backup()
    o.operation()
    c.backup()
    o.operation()
    c.show_history()

    print('\nClient: now, lets roll back!')
    c.undo()
    c.show_history()

if __name__ == '__main__':
    client_code()