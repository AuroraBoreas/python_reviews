
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
        print(f'{self.__class__} handles the {request}')

class Invoker:
    def __init__(self) -> None:
        self._commands:List[Command] = []

    def add(self, command:Command) -> None:
        self._commands.append(command)

    def run(self) -> None:
        for cmd in self._commands:
            cmd.execute()

def client_code() -> None:
    cmd1 = Command(Receiver(), "hello")
    cmd2 = Command(Receiver(), "world")
    inv  = Invoker()
    inv.add(cmd1)
    inv.add(cmd2)
    inv.run()

if __name__ == '__main__':
    client_code()