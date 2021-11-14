# caretaker - (originator - memento)

from abc import ABCMeta, abstractmethod
import datetime
import random
import string
from typing import List

class IMemento(metaclass=ABCMeta):
    @abstractmethod
    def get_state(self)->str:
        pass

    @abstractmethod
    def get_name(self)->str:
        pass

    @abstractmethod
    def get_date(self)->str:
        pass

class Memento(IMemento):
    def __init__(self, state:str) -> None:
        self._state = state
        self._date = str(datetime.datetime.now())[:19]

    def get_state(self) -> str:
        return self._state

    def get_date(self) -> str:
        return self._date

    def get_name(self) -> str:
        return f'({self._date}) / ({self._state[:9]})'
    
class Originator:
    _state:str = None

    def __init__(self, state:str) -> None:
        self._state = state

    def operation(self)->None:
        self._generate_random_string(30)

    def _generate_random_string(self, length:int=10)->None:
        self._state = ''.join(random.sample(string.ascii_letters, length))

    def save(self)->Memento:
        return Memento(self._state)

    def restore(self, memento:Memento)->None:
        self._state = memento.get_state()

class Caretaker:
    def __init__(self, originator:Originator) -> None:
        self._originator = originator
        self._mementos:List[Memento] = []

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
    o = Originator('zhangliangcy')
    c = Caretaker(o)

    c.backup()
    o.operation()

    c.backup()
    o.operation()

    c.backup()
    o.operation()

    c.show_history()

    print('Client: now, lets roll back!')
    c.undo()
    print(f'and originator state: {o._state}')
    
    print()
    c.show_history()

if __name__ == '__main__':
    client_code()