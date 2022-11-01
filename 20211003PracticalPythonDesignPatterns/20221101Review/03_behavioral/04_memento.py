"#" 

from abc import ABC, abstractmethod
import datetime
import string, random
from typing import List

class IMemento(ABC):
    @abstractmethod
    def get_state(self) -> str:
        raise NotImplementedError()
    @abstractmethod
    def get_date(self) -> str:
        raise NotImplementedError()
    @abstractmethod
    def get_name(self) -> str:
        raise NotImplementedError()

class Memento(IMemento):
    def __init__(self, state:str) -> None:
        self._date = str(datetime.datetime.now())[:19]
        self._state = state    
    def get_date(self) -> str:
        return self._date    
    def get_state(self) -> str:
        return self._state
    def get_name(self) -> str:
        return f'{self._date} / {self._state}'

class Originator:
    _state:str = None
    def __init__(self) -> None:
        pass
    def save(self) -> Memento:
        return Memento(self._state)
    def restore(self, memento:Memento) -> None:
        self._state = memento.get_state()
    def __generate_random_string(self, length:int=10) -> None:
        self._state = ''.join(random.sample(string.ascii_letters, length))
    def operate(self) -> None:
        self.__generate_random_string(30)

class Caretaker:
    _mementos:List[Memento] = list()

    def __init__(self, o:Originator) -> None:
        self._o = o
    def backup(self) -> None:
        self._mementos.append(self._o.save())
    def undo(self) -> None:
        if not self._mementos:
            return
        memento = self._mementos.pop()
        try:
            self._o.restore(memento)
        except Exception:
            self.undo()
    def list_history(self) -> str:
        return 'memento history: \n{}'.format('\n'.join(m.get_name() for m in self._mementos))