"Python is a protocol orientated language; every top-level function implements its dunder method;" 

from __future__ import annotations

class Command:
    def __init__(self, rec: Receiver, req: str) -> None:
        self.rec = rec
        self.req = req

    def execute(self) -> None:
        self.rec.operate(self.req)

class Receiver:
    def operate(self, request: str) -> None:
        print(f"{self.__class__} handles {request}")

class Invoker:
    def __init__(self) -> None:
        self._commands: list[Command] = list()
    
    def add(self, command: Command) -> None:
        self._commands.append(command)

    def run(self) -> None:
        for command in self._commands:
            command.execute()