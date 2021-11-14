# Caretaker - Originator - Memento

from __future__ import annotations
from abc import ABC, abstractmethod
import string
import random
import datetime
from typing import List

class Originator:
    _state:str = None

    def __init__(self, state:str) -> None:
        self._state = state
        print(f'Originator: my initial state is: {self._state}')

    def do_something(self)->None:
        self._state = self._generate_random_string(30)

    def _generate_random_string(self, n=10)->str:
        return ''.join(random.sample(string.ascii_letters, n))

    def restore(self, memento:Memento)->None:
        self._state = memento.get_state()

    def save(self)->Memento:
        return ConcreteMemento(self._state)

class Memento(ABC):
    @abstractmethod
    def get_name(self)->str:
        pass

    @abstractmethod
    def get_date(self)->str:
        pass

class ConcreteMemento(Memento):
    def __init__(self, state:str) -> None:
        self._state = state
        self._date = str(datetime.datetime.now())[:19]

    def get_name(self) -> str:
        return f'{self._date} / ({self._state[0:9]}...)'

    def get_date(self) -> str:
        return self._date

    def get_state(self)->str:
        return self._state

class Caretaker:
    def __init__(self, originator:Originator) -> None:
        self._mementos:List[Memento] = []
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
            print(memento.get_name())

def client_code()->None:
    o = Originator('hello zhang liang')
    c = Caretaker(o)

    c.backup()
    o.do_something()
    
    c.backup()
    o.do_something()

    c.backup()
    o.do_something()

    c.show_history()
    c.undo()

    c.undo()

 
if __name__ == '__main__':
    client_code()
