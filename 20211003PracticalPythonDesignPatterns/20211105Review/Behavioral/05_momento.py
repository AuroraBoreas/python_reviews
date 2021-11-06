# undo
from __future__ import annotations
from abc import ABCMeta, abstractmethod
import random
import string
import datetime

class Memento:
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_name(self)->str:
        pass

    @abstractmethod
    def get_date(self)->str:
        pass

class ConcreteMemento(Memento):
    def __init__(self, state:str) -> None:
        self._state = state
        self._date = str(datetime.datetime.now())[:10]

    def get_state(self)->str:
        return self._state

    def get_name(self) -> str:
        return f'{self._date} / ({self._state[0:9]})'

    def get_date(self) -> str:
        return self._date

class Caretaker:
    def __init__(self, originator:Originator) -> None:
        self._mementos = []
        self._originator = originator

    def backup(self)->None:
        print(f"\nCaretaker: Saving Originator's state..")
        self._mementos.append(self._originator.save())
    
    def undo(self)->None:
        if not len(self._mementos):
            return
        memento:Memento = self._mementos.pop()
        print(f'Caretaker: restoring state to: {memento.get_name()}')
        try:
            self._originator.restore(memento)
        except Exception:
            self.undo()

    def show_history(self)->None:
        print('Caretaker: here is the list of memento:')
        for memento in self._mementos:
            print(memento.get_name())

class Originator:
    _state:str = None
    
    def __init__(self, state:str) -> None:
        self._state = state
        print(f'originator: My initial state is: {self._state}')

    def do_something(self)->None:
        print('originator: im doing something important...')
        self._state = self._generate_random_string(30)
        print(f'originator: and my state has changed to: {self._state}')

    def _generate_random_string(self, length:int=10)->None:
        return ''.join(random.sample(string.ascii_letters, length))

    def save(self)->Memento:
        return ConcreteMemento(self._state)

    def restore(self, memento:Memento)->None:
        self._state = memento.get_state()
        print(f'originator: my state has changed to: {self._state}')

def client_code()->None:
    ori = Originator('Super-duper-super-puper-super')
    car = Caretaker(ori)

    car.backup()
    ori.do_something()

    car.backup()
    ori.do_something()

    car.backup()
    ori.do_something()

    car.backup()
    ori.do_something()

    print()
    car.show_history()

    print('\nclient: now, let\'s roll back!\n')
    car.undo()

    print('\nclient: once more!\n')
    car.undo()

if __name__ == '__main__':
    client_code()