# invoker - receiver - command 

from typing import List


class Receiver:
    def operation(self, request:str)->None:
        print(f'{request} received, start processing..')

class Command:
    def __init__(self, receiver:Receiver, request:str) -> None:
        self.receiver = receiver
        self.request = request

    def execute(self)->None:
        self.receiver.operation(self.request)

class Invoker:
    def __init__(self) -> None:
        self._commands:List[Command] = []

    def add(self, command:Command)->None:
        self._commands.append(command)

    def run(self)->None:
        for command in self._commands:
            command.execute()

def client_code()->None:
    r = Receiver()
    c1 = Command(r, 'command 1')
    c2 = Command(r, 'command 2')
    inv = Invoker()
    inv.add(c1)
    inv.add(c2)
    inv.run()
