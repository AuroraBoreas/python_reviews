"#" 
from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import datetime
import random
import string
from typing import List


class Caretaker:
    _mementos:List[Memento] = []
    
    def __init__(self, o:Originator) -> None:
        self._o = o
    
    def backup(self)->None:
        self._mementos.append(self._o.save())

    def undo(self)->None:
        if not self._mementos:
            return
        else:
            memento = self._mementos.pop()
            try:
                self._o.restore(memento)
            except Exception:
                self.restore()

    def list_mementos(self)->None:
        print('history :\n{}'.format("\n".join([m.get_info() for m in self._mementos])))

class Originator:
    _state:str = None

    def __init__(self, state:str) -> None:
        self._state = state

    def save(self)->Memento:
        return Memento(self._state)

    def restore(self, memento:Memento)->None:
        self._state = memento.get_state()

    def generate_random_string(self, length:int=10)->None:
        return ''.join([random.choice(string.ascii_letters) for _ in range(length)])

    def operation(self)->None:
        self._state = self.generate_random_string(30)

class IMemento(ABC):
    @abstractmethod
    def get_date(self)->str: pass

    @abstractmethod
    def get_state(self)->str: pass

    @abstractmethod
    def get_info(self)->str: pass

class Memento(IMemento):
    def __init__(self, state:str) -> None:
        self._date  = str(datetime.now())[:19]
        self._state = state
    
    def get_date(self) -> str:
        return self._date

    def get_state(self) -> str:
        return self._state

    def get_info(self) -> str:
        return f'({self._date}) / ({self._state[:9]})'