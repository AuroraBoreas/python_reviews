# 

from abc import ABC, abstractmethod
import datetime
import random
import string
from typing import List


class IMemento(ABC):
    @abstractmethod
    def get_state(self)->str: pass

    @abstractmethod
    def get_date(self)->str: pass

    @abstractmethod
    def get_text(self)->str: pass

class Memento(IMemento):
    def __init__(self, state:str) -> None:
        self._state = state
        self._date  = str(datetime.datetime.now())[:19]

    def get_text(self) -> str:
        return f'({self._date}) / ({self._state[:9]})'

    def get_date(self) -> str:
        return self._date

    def get_state(self) -> str:
        return self._state

class Originator:
    _state:str = None

    def __init__(self, state:str) -> None:
        self._state = state

    def save(self)->Memento:
        return Memento(self._state)

    def restore(self, memento:Memento)->None:
        self._state = memento.get_state()

    def _generate_random_string(self, length:int=10)->None:
        self._state = ''.join(random.sample(string.ascii_letters, length))

    def operation(self)->None:
        self._generate_random_string(30)

class Caretaker:
    _mementos:List[Memento] = []

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
        print('\n'.join(map(str, [m.get_text() for m in self._mementos])))