"Python is a protocol orientated language; every top-level function implements its dunder method;" 

from abc import ABC, abstractmethod
import datetime
import random
import string

class IMemento(ABC):
    @abstractmethod
    def get_state(self) -> str:
        raise NotImplementedError
    
    @abstractmethod
    def get_info(self) -> str:
        raise NotImplementedError
    
    @abstractmethod
    def get_date(self) -> str:
        raise NotImplementedError
    
class Memento1(IMemento):
    def __init__(self, state: str) -> None:
        self._state = state
        self._date = str(datetime.datetime.today())[:19]
    
    def get_date(self) -> str:
        return self._date
    
    def get_state(self) -> str:
        return self._state
    
    def get_info(self) -> str:
        return f'{self._date} / {self._state[:10]}'

class Originator:
    _state: str = None

    def __init__(self) -> None:
        pass

    def save(self) -> IMemento:
        return Memento1(self._state)

    def undo(self, memento: IMemento) -> None:
        self._state = memento.get_state()

    def __generate_string(self, length: int=10) -> None:
        self._state = ''.join(random.sample(string.ascii_letters, length))

    def operate(self) -> None:
        self.__generate_string(30)

class Caretaker:
    mementos: list[IMemento] = list()

    def __init__(self, o: Originator) -> None:
        self._o = o

    def backup(self) -> None:
        self.mementos.append(self._o.save())

    def restore(self) -> None:
        if not self.mementos:
            return
        memento: IMemento = self.mementos.pop()
        try:
            self._o.undo(memento)
        except Exception:
            self.restore()
    
    def show(self) -> str:
        return "history:\n{0}".format("\n".join(m.get_info() for m in self.mementos))

def client_code() -> None:
    o: Originator = Originator()
    c: Caretaker = Caretaker(o)
    o.operate()
    c.backup()
    o.operate()
    c.backup()
    print(c.show())
    c.restore()
    print(c.show())

def main() -> None:
    client_code()

if __name__ == '__main__':
    main()
