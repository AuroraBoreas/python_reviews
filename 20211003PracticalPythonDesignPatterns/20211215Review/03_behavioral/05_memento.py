# 
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
import random
import string
import datetime

class Caretaker:
    _mementos:List[Mememto] = []

    def __init__(self, originator:Originator) -> None:
        self._originator = originator

    def backup(self)->None:
        self._mementos.append(self._originator.save())

    def undo(self)->None:
        if not self._mementos:
            return
        memento = self._mementos.pop()
        try:
            self._originator.restore(memento)
        except Exception:
            self.undo()

    def list_history(self)->None:
        print('\n'.join(self._mementos))

class Originator:
    _state:str = None

    def __init__(self, state:str) -> None:
        self._state = state

    def save(self)->Mememto:
        return Mememto(self._state)
    
    def restore(self, memento:Mememto)->None:
        self._state = memento.get_state()

    def _generate_random_string(self, length:int=10)->None:
        self._state = ''.join(random.sample(string.ascii_letters, length))

    def operation(self)->None:
        self._generate_random_string(30)

class IMemento(ABC):
    @abstractmethod
    def get_state(self)->str: pass

    @abstractmethod
    def get_date(self)->str: pass

    @abstractmethod
    def get_name(self)->str: pass


class Mememto(IMemento):
    def __init__(self, state:str) -> None:
        self._state = state
        self._date = str(datetime.datetime.now())[:19]

    def get_date(self) -> str:
        return self._date

    def get_name(self) -> str:
        return f'({self._date}) / ({self._state[:9]})'

    def get_state(self) -> str:
        return self._state