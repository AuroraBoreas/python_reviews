"#" 

from __future__ import annotations
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

class Command:
    def __init__(self, rec: Receiver, req: str) -> None:
        self._rec = rec
        self._req = req

    def execute(self) -> None:
        self._rec.operate(self._req)

class Receiver:
    def operate(self, request: str) -> None:
        logging.info(f"{self.__class__} handles {request}")        

class Invoker:
    def __init__(self) -> None:
        self._commands: list[Command] = []

    def add(self, command: Command) -> None:
        self._commands.append(command)

    def remove(self, command: Command) -> None:
        self._commands.remove(command)

    def run(self) -> None:
        for command in self._commands:
            command.execute()

def main() -> None:
    i: Invoker = Invoker()
    i.add(Command(Receiver(), "hello"))
    i.add(Command(Receiver(), "world"))
    i.add(Command(Receiver(), "!"))
    i.run()

if __name__ == '__main__':
    main()
