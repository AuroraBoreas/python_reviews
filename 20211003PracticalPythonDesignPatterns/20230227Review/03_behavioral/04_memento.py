# 

from abc import ABC, abstractmethod
import datetime
import random
import string


class IMemento(ABC):
    @abstractmethod
    def get_state(self) -> str:
        pass
    @abstractmethod
    def get_name(self) -> str:
        pass
    @abstractmethod
    def get_date(self) -> str:
        pass

class Memento1(IMemento):
    def __init__(self, state: str) -> None:
        self._state = state
        self._date = datetime.datetime.now().__str__()[:19]

    def get_date(self) -> str:
        return self._date

    def get_name(self) -> str:
        return f'{self._date} / {self._state[:9]}'
    
    def get_state(self) -> str:
        return self._state
    
class Originator:
    _state: str = None

    def __init__(self, state: str) -> None:
        self._state = state

    def save(self) -> IMemento:
        return Memento1(self._state)

    def restore(self, memento: IMemento) -> None:
        self._state = memento.get_state()

    def _generate_random_string(self, length: int=10) -> None:
        self._state = ''.join(random.sample(string.ascii_letters, length))

    def operate(self) -> None:
        self._generate_random_string(30)

class Caretaker:
    _mementos: list[IMemento] = list()

    def __init__(self, o: Originator) -> None:
        self._o = o
    
    def backup(self) -> None:
        self._mementos.append(self._o.save())

    def undo(self) -> None:
        if not self._mementos:
            return
        memento: IMemento = self._mementos.pop()
        try:
            self._o.restore(memento)
        except Exception:
            self.undo()

    def show_history(self) -> None:
        print("history:\n{}".format('\n'.join(m.get_name() for m in self._mementos)))

def client_code() -> None:
    o: Originator = Originator("hello world")
    c: Caretaker = Caretaker(o)
    c.backup()
    o.operate()
    c.backup()
    o.operate()
    c.backup()
    c.show_history()
    print(o._state)
    c.undo()
    print(o._state)
    c.undo()
    print(o._state)

def main() -> None:
    client_code()

if __name__ == '__main__':
    main()
