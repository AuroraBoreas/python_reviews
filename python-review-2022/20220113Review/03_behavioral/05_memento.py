# 
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
import random, string, datetime

class Caretaker:
    _mementos:List[IMemento] = []

    def __init__(self, o:Originator) -> None:
        self._o = o

    def backup(self)->None:
        self._mementos.append(self._o.save())

    def undo(self)->None:
        if not self._mementos:
            return
        memento = self._mementos.pop()
        try:
            self._o.restore(memento)
        except Exception:
            self.undo()

    def list_history(self)->None:
        print('\n'.join(map(str, [m.get_name() for m in self._mementos])))

class Originator:
    _state:str = None

    def __init__(self) -> None:
        pass
    
    def save(self)->IMemento:
        return Memento(self._state)

    def restore(self, memento:IMemento)->None:
        self._state = memento.get_state()

    def _generate_random_string(self, length:int=10)->None:
        self._state = ''.join(random.sample(string.ascii_letters, length))

    def operation(self)->None:
        self._generate_random_string(30)

class IMemento(ABC):
    @abstractmethod
    def get_name(self)->str: pass

    @abstractmethod
    def get_state(self)->str: pass

    @abstractmethod
    def get_date(sellf)->str: pass

class Memento(IMemento):
    def __init__(self, state:str) -> None:
        self._state = state
        self._date  = str(datetime.dateimte.now())[:19]

    def get_date(self) -> str:
        return self._date

    def get_name(self) -> str:
        return f'({self._date}) / ({self._state[:9]})'

    def get_state(self) -> str:
        return self._state