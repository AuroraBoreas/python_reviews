# 
from __future__ import annotations

class Command:
    def __init__(self, rec: Receiver, req: str) -> None:
        self._rec = rec
        self._req = req

    def operate(self) -> None:
        print(self._rec.handle(self._req))

class Receiver:
    def handle(self, req: str) -> str:
        return f'{self.__class__} handles {req}'

class Invoker:
    def __init__(self) -> None:
        self._commands: list[Command] = []

    def add(self, command: Command) -> None:
        self._commands.append(command)

    def run(self) -> None:
        for command in self._commands:
            command.operate()

def client_code() -> None:
    i: Invoker = Invoker()
    i.add(Command(Receiver(), 'hello'))
    i.add(Command(Receiver(), 'world'))
    i.add(Command(Receiver(), 'Goodness'))
    i.run()

def main() -> None:
    client_code()

if __name__ == '__main__':
    main()