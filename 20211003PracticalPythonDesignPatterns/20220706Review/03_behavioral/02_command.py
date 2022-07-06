# 
from __future__ import annotations
from typing import Any, List


class Command:
    def __init__(self, rec:Receiver, req:str) -> None:
        self._rec = rec
        self._req = req
    
    def execute(self) -> Any:
        return self._rec.operate(self._req)

class Receiver:
    def operate(self, request:str) -> str:
        return f'{self.__class__} handle {request}'

class Invoker:
    def __init__(self) -> None:
        self._commands:List[Command] = list()

    def add(self, cmd:Command) -> None:
        self._commands.append(cmd)

    def remove(self, cmd:Command) -> None:
        self._commands.remove(cmd)

    def run(self) -> None:
        for cmd in self._commands:
            print(cmd.execute())

def client_code() -> None:
    i = Invoker()
    i.add(Command(Receiver(), 'awake'))
    i.add(Command(Receiver(), 'wash'))
    i.add(Command(Receiver(), 'clean'))
    i.add(Command(Receiver(), 'work'))
    i.run()

if __name__ == '__main__':
    client_code()