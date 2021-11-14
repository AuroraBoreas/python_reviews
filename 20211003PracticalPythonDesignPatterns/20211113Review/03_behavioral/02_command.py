# command - receiver - invoker
from __future__ import annotations
from typing import List

class Command:
    def __init__(self, receiver:Receiver, request:str) -> None:
        self.receiver = receiver
        self.request  = request
    
    def execute(self)->None:
        self.receiver.do(self.request)

class Receiver:
    def do(self, request:str)->None:
        print(f'{request} received, start processing..')

class Invoker:
    def __init__(self) -> None:
        self.commands:List[Command] = []

    def add(self, command:Command)->None:
        self.commands.append(command)

    def run(self)->None:
        for command in self.commands:
            command.execute()

def client_code()->None:
    r  = Receiver()
    c1 = Command(r, 'command 1')
    c2 = Command(r, 'command 2')
    invoker = Invoker()
    invoker.add(c1)
    invoker.add(c2)
    invoker.run()

if __name__ == '__main__':
    client_code()
