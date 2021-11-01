# command
from __future__ import annotations

class Command:
    def __init__(self, receiver:Receiver, msg:str) -> None:
        self.receiver = receiver
        self.msg = msg

    def execute(self)->None:
        self.receiver.do_this(self.msg)

class Receiver:
    def __init__(self) -> None:
        pass

    def do_this(self, msg:str)->None:
        print(f'received, start {msg}')


class Invoker:
    def __init__(self) -> None:
        self.commands = []

    def add(self, command:Command)->None:
        self.commands.append(command)

    def run(self)->None:
        for command in self.commands:
            command.execute()


def client_code():
    r = Receiver()
    c1 = Command(r, 'command 1')
    c2 = Command(r, 'command 2')
    inv = Invoker()
    inv.add(c1)
    inv.add(c2)
    inv.run()

if __name__ == '__main__':
    client_code()