#

from abc import ABC, abstractmethod
from datetime import datetime
import random, string
from typing import List

class IMemento(ABC):
    @abstractmethod
    def get_date(self) -> str:
        raise NotImplementedError()

    @abstractmethod
    def get_text(self) -> str:
        raise NotImplementedError()

    @abstractmethod
    def get_state(self) -> str:
        raise NotImplementedError()

class Memento(IMemento):
    def __init__(self, state:str) -> None:
        self._state = state
        self._date = str(datetime.now())[:19]
    
    def get_date(self) -> str:
        return self._date

    def get_state(self) -> str:
        return self._state

    def get_text(self) -> str:
        return '{} / {}'.format(self._date, self._state[:7])

class Originator:
    _state:str = None

    def __init__(self, state:str) -> None:
        self._state = state
    
    def save(self) -> Memento:
        return Memento(self._state)
    
    def undo(self, memento:Memento) -> None:
        self._state = memento.get_state()

    def _generate_random_string(self, length:int=10) -> None:
        self._state = ''.join(random.sample(string.ascii_letters, length))

    def operate(self) -> None:
        self._generate_random_string(30)

class Caretaker:
    mementos:List[Memento] = list()
    
    def __init__(self, o:Originator) -> None:
        self._o = o
    
    def backup(self) -> None:
        self.mementos.append(self._o.save())

    def restore(self) -> None:
        if not self.mementos:
            return
        memento = self.mementos.pop()
        try:
            self._o.undo(memento)
        except Exception:
            self.restore()

    def show_history(self) -> None:
        return '\n'.join(m.get_text() for m in self.mementos)

def client_code() -> None:
    o = Originator("hello world")
    c = Caretaker(o)
    c.backup()
    o.operate()
    c.backup()
    o.operate()
    c.backup()
    print(c.show_history())
    print('\nroll back')
    c.restore()
    print(c.show_history())

if __name__ == '__main__':
    client_code()