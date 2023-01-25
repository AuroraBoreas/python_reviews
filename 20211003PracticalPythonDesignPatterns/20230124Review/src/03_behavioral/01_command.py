from __future__ import annotations
from typing import Any


class Command:
    def __init__(self, rec: Receiver, req: str) -> None:
        self._rec = rec
        self._req = req

    def execute(self) -> Any:
        return self._rec.handle(self._req)

class Receiver:
    def handle(self, request: str) -> str:
        return f"{self.__class__} handles {request}"

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
