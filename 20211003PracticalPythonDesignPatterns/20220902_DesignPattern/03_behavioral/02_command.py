"#" 
from __future__ import annotations
from typing import List


class Command:
    def __init__(self, rec:Receiver, req:str) -> None:
        self._rec = rec
        self._req = req

    def execute(self) -> None:
        self._rec.handle(self._req)

class Receiver:
    def handle(self, request:str) -> None:
        print(f'{self.__class__} handle {request}')

class Invoker:
    def __init__(self) -> None:
        self._commands:List[Command] = []

    def add(self, cmd:Command) -> None:
        self._commands.append(cmd)

    def run(self) -> None:
        for cmd in self._commands:
            cmd.execute()

def client_code() -> None:
    inv:Invoker = Invoker()
    inv.add(Command(Receiver(), 'aic'))
    inv.add(Command(Receiver(), 'pismoea'))
    inv.add(Command(Receiver(), 'sipoc'))
    inv.run()

if __name__ == '__main__':
    client_code()