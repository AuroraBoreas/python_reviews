"#" 

from abc import ABC, abstractmethod
from http import client
import random, string, datetime
from typing import List


class IMemento(ABC):
    @abstractmethod
    def get_date(self) -> str:
        raise NotImplementedError()
    
    @abstractmethod
    def get_state(self) -> str:
        raise NotImplementedError()

    @abstractmethod
    def get_name(self) -> str:
        raise NotImplementedError()

class Memento(IMemento):
    def __init__(self, state:str) -> None:
        self._state = state
        self._date  = str(datetime.datetime.now())[:19]

    def get_name(self) -> str:
        return f'{self._date} / {self._state[:9]}'

    def get_date(self) -> str:
        return self._date

    def get_state(self) -> str:
        return self._state

class Originator:
    _state:str = None

    def __init__(self, state:str) -> None:
        self._state = state

    def save(self) -> IMemento:
        return Memento(self._state)

    def restore(self, m:IMemento) -> None:
        self._state = m.get_state()

    def __generate_random_string(self, length:int=10) -> str:
        return ''.join(random.sample(string.ascii_letters, length))

    def operate(self) -> None:
        self._state = self.__generate_random_string(30)

class Caretaker:
    _mementos:List[Memento] = []

    def __init__(self, o:Originator) -> None:
        self._o = o
        
    def backup(self) -> None:
        self._mementos.append(self._o.save())    

    def undo(self) -> None:
        if not self._mementos:
            return None
        m:Memento = self._mementos.pop()
        try:
            self._o.restore(m)
        except Exception:
            self.undo()
    
    def list_history(self) -> None:
        print(f'{self.__class__} history:')
        print('\n'.join(m.get_name() for m in self._mementos))

def client_code() -> None:
    o:Originator = Originator("hello world")
    c:Caretaker = Caretaker(o)
    o.operate()
    c.backup()
    o.operate()
    c.backup()
    o.operate()
    c.backup()
    c.list_history()
    c.undo()
    c.list_history()
    print(o._state)

if __name__ == '__main__':
    client_code()



