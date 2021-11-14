# caretake - [originator - memento]; using stack concept
from __future__ import annotations
from abc import ABC, abstractmethod
import datetime
import random
import string
from typing import List

class Originator:
    _state:str = None

    def __init__(self, state:str) -> None:
        self._state = state
        print(f'{self.__class__}: my initial state is: {self._state}')

    def do_something(self)->None:
        print(f'{self.__class__}: im doing something important..')
        self._state = self._generate_random_string(30)
        print(f'{self.__class__}: and my state changed to: {self._state}')

    def _generate_random_string(self, length:int=10)->None:
        return ''.join(random.sample(string.ascii_letters, length))

    def save(self)->Memento:
        return ConcreteMemento(self._state)

    def restor(self, memento:Memento)->None:
        self._state = memento.get_state()

class Memento(ABC):
    @abstractmethod
    def get_name(self)->str: pass

    @abstractmethod
    def get_date(self)->str: pass

    @abstractmethod
    def get_state(self)->str: pass

class ConcreteMemento(Memento):
    def __init__(self, state:str) -> None:
        self._state = state
        self._date  = str(datetime.datetime.now())[:19]

    def get_date(self) -> str:
        return self._date
    
    def get_name(self) -> str:
        return f'({self._date}) / ({self._state[0:9]})'

    def get_state(self)->str:
        return self._state

class Caretaker:
    def __init__(self, originator:Originator=None) -> None:
        self._mementos:List[Memento] = []
        self._originator = originator
    
    def backup(self)->None:
        print(f'{self.__class__}: saving originator\'s state..')
        self._mementos.append(self._originator.save())

    def undo(self)->None:
        if not len(self._mementos):
            return

        memento = self._mementos.pop()
        print(f'{self.__class__}: restoring state to: {memento.get_name()}')
        try:
            self._originator.restor(memento)
        except Exception:
            self.undo()
    
    def show_history(self)->None:
        print(f'{self.__class__}: here\'s the list of mementos:')
        for memento in self._mementos:
            print(memento.get_name())

def client_code()->None:
    o = Originator('zhangliang - scy')
    c = Caretaker(o)
    c.backup()
    o.do_something()
    
    c.backup()
    o.do_something()

    c.backup()
    o.do_something()

    print()
    c.show_history()

    print('\nClient: now, lets roll back!')
    c.undo()

    print('\nClient: Once more\n')
    c.undo()

if __name__ == '__main__':
    client_code()
