# invoker - receiver - command 
from __future__ import annotations
from typing import List


class Command:
    def __init__(self, receiver:Receiver, request:str) -> None:
        self.receiver = receiver
        self.request = request
    
    def execute(self)->None:
        self.receiver.operation(self.request)

class Receiver:
    def operation(self, request:str)->None:
        print(f'{self.__class__} received request ({request}), start processing..')

class Invoker:
    def __init__(self) -> None:
        self.commands:List[Command] = []
    
    def add(self, command:Command)->None:
        self.commands.append(command)

    def run(self)->None:
        for command in self.commands:
            command.execute()

def client_code()->None:
    r = Receiver()
    c1 = Command(r, 'command 1')
    c2 = Command(r, 'command 2')
    inv = Invoker()
    inv.add(c1)
    inv.add(c2)
    inv.run()