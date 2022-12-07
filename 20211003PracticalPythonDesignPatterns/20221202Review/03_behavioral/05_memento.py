"#" 

from abc import abstractmethod
import datetime
import random
import string
from typing import List


class IMemento:
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

    def get_state(self) -> str:
        return self._state
    def get_date(self) -> str:
        return self._date
    def get_name(self) -> str:
        return f'{self._date} / {self._state[:10]}'

class Originator:
    __state:str = None

    def __init__(self, state:str) -> None:
        self.__state = state

    def save(self) -> IMemento:
        return Memento(self.__state)

    def restore(self, memento:IMemento) -> None:
        self.__state = memento.get_state()

    def _generate_random_string(self, length:int=10) -> None:
        self.__state = ''.join(random.sample(string.ascii_letters, length))

    def operate(self) -> None:
        self._generate_random_string(30)

    @property
    def state(self) -> str:
        return self.__state

class Caretaker:
    __mementos:List[IMemento] = []

    def __init__(self, o:Originator) -> None:
        self._o = o

    def backup(self) -> None:
        self.__mementos.append(self._o.save())

    def undo(self) -> None:
        if not self.__mementos:
            return
        memento = self.__mementos.pop()
        try:
            self._o.restore(memento)
        except Exception:
            self.undo()

    def list_history(self) -> None:
        print('history:\n{}'.format('\n'.join([m.get_name() for m in self.__mementos])))

def client_code() -> None:
    o = Originator("hello world!")
    c = Caretaker(o)
    c.backup()
    o.operate()
    c.backup()
    o.operate()
    c.backup()
    c.list_history()
    print('roll back')
    c.undo()
    c.list_history()
    print(o.state)

if __name__ == '__main__':
    client_code()
