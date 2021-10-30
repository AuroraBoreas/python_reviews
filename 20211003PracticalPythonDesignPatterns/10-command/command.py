# command
from __future__ import annotations
from typing import ContextManager

class Command:
    def __init__(self, receiver:Receiver, what:str)->None:
        self.recerver = receiver
        self.what = what

    def execute(self)->None:
        self.recerver.do(self.what)


class Receiver:
    def do(self, what:str)->None:
        print(f'received request, start to {what}')


class Invoker:
    def __init__(self)->None:
        self.commands = []

    def add(self, command:Command)->None:
        self.commands.append(command)

    def run(self)->None:
        for command in self.commands:
            command.execute()

def client_code()->None:
    r = Receiver()
    c1 = Command(r, 'drink milk')
    c2 = Command(r, 'eat apple')
    inv = Invoker()
    inv.add(c1)
    inv.add(c2)
    inv.run()

if __name__ == '__main__':
    client_code()
    