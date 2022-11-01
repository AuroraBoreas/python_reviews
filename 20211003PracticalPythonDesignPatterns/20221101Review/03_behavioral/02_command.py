"#" 
from __future__ import annotations
from typing import Any, List


class Command:
    def __init__(self, rec:Receiver, req:str) -> None:
        self._rec = rec
        self._req = req

    def execute(self) -> None:
        self._rec.handle(self._req)

class Receiver:
    def handle(self, request:Any) -> None:
        print(f'{self.__class__} handle {request}')


class Invoker:
    def __init__(self) -> None:
        self._commands:List[Command] = list()
    
    def add(self, cmd:Command) -> None:
        self._commands.append(cmd)
    
    def remove(self, cmd:Command) -> None:
        self._commands.remove(cmd)

    def run(self) -> None:
        for cmd in self._commands:
            cmd.execute()
