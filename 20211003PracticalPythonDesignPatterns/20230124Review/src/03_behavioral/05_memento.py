
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
        self._date: str = str(datetime.datetime.now())[:19]

    def get_date(self) -> str:
        return self._date

    def get_state(self) -> str:
        return self._state

    def get_info(self) -> str:
        return f"{self._date} / {self._state[:9]}"

class Origiantor:
    state: str = None

    def __init__(self) -> None:
        pass

    def save(self) -> IMemento:
        return Memento1(self.state)

    def restore(self, memento: IMemento) -> None:
        self.state = memento.get_state()

    def _generate_string(length: int=10) -> str:
        return ''.join(random.sample(string.ascii_letters, length))

    def operate(self) -> None:
        self.state = self._generate_string(30)

class Caretaker:
    mementos: list[IMemento] = list()

    def __init__(self, o: Origiantor) -> None:
        self._o = o

    def backup(self) -> None:
        self.mementos.append(self._o.save())

    def undo(self) -> None:
        if not self.mementos:
            return
        memento: IMemento = self.mementos.pop()
        try:
            self._o.restore(memento)
        except Exception:
            self.undo()

    def show_history(self) -> str:
        return "history:\n {0}".format("\n".join(m.get_info() for m in self.mementos))
