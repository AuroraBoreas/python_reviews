"#" 
from __future__ import annotations
from typing import List


class Command:
    def __init__(self, rec:Receiver, req:str) -> None:
        self._rec = rec
        self._req = req

    def operate(self) -> None:
        self._rec.handle(self._req)

class Receiver:
    def handle(self, request:str) -> None:
        print(f'{self.__class__} handle {request}')

class Invoker:
    def __init__(self) -> None:
        self._commands:List[Command] = []

    def add(self, command:Command) -> None:
        self._commands.append(command)
    
    def remove(self, command:Command) -> None:
        self._commands.remove(command)

    def run(self) -> None:
        for command in self._commands:
            command.operate()

def client_code() -> None:
    i = Invoker()
    i.add(Command(Receiver(), 'hello'))
    i.add(Command(Receiver(), 'world'))
    i.run()

if __name__ == '__main__':
    client_code()