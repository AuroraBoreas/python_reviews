# 

from abc import ABC, abstractmethod
import datetime, random
import string
from typing import List

class IMemento(ABC):
    @abstractmethod
    def get_state(self) -> str: pass

    @abstractmethod
    def get_name(self) -> str: pass

    @abstractmethod
    def get_date(self) -> str: pass

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

class Originator:
    _state:str = None

    def __init__(self, state:str) -> None:
        self._state = state

    def save(self) -> Memento:
        return Memento(self._state)

    def restore(self, memento:Memento) -> None:
        self._state = memento.get_state()

    def _generate_random_string(self, length:int=10) -> str:
        return ''.join(random.sample(string.ascii_letters, length))

    def operate(self) -> None:
        self._state = self._generate_random_string(30)

class Caretaker:
    _mementos:List[Memento] = list()

    def __init__(self, o:Originator) -> None:
        self._o = o
    
    def backup(self) -> None:
        self._mementos.append(self._o.save())

    def restore(self) -> None:
        if not self._mementos:
            return
        memento = self._mementos.pop()
        try:
            self._o.restore(memento)
        except Exception:
            self.restore()

    def show_history(self) -> None:
        print('history:\n{}'.format("\n".join([m.get_name() for m in self._mementos])))

def client_code() -> None:
    o = Originator("hello world!")
    c = Caretaker(o)
    c.backup()
    o.operate()
    c.backup()
    o.operate()
    c.backup()
    c.show_history()
    print(o._state)
    c.restore()
    print(o._state)
    c.restore()
    print(o._state)
    c.show_history()
    

if __name__ == '__main__':
    client_code()