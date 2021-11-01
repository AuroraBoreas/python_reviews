# command
from __future__ import annotations

class Command:
    def __init__(self, receiver:Receiver, request:str) -> None:
        self.receiver = receiver
        self.request = request

    def execute(self)->None:
        self.receiver.cook(self.request)

class Receiver:
    def cook(self, food:str)->None:
        print(f'{food} request is received, start cooking..')

class Invoker:
    def __init__(self) -> None:
        self.commands = []

    def add(self, command:Command)->None:
        self.commands.append(command)
    
    def run(self):
        for command in self.commands:
            command.execute()

if __name__ == '__main__':
    r = Receiver()
    c1 = Command(r, 'meatball')
    c2 = Command(r, 'coffee')
    c3 = Command(r, 'beef')
    i = Invoker()
    i.add(c1)
    i.add(c2)
    i.add(c3)
    i.run()