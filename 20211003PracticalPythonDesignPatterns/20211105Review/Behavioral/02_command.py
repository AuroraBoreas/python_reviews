# command
from __future__ import annotations

class Command:
    def __init__(self, receiver:Receiver, msg:str)->None:
        self.receiver = receiver
        self.msg = msg

    def execute(self)->None:
        self.receiver.print_msg(self.msg)

class Receiver:
    def print_msg(self, msg:str)->None:
        print(f'{msg} received, start processing..')

class Invoker:
    def __init__(self) -> None:
        self.commands = []

    def add(self, command:Command)->None:
        self.commands.append(command)
        
    def run(self)->None:
        for command in self.commands:
            command.execute()

def client_code()->None:
    r = Receiver()
    cmd1 = Command(r, 'command 1')
    cmd2 = Command(r, 'command 2')
    i = Invoker()
    i.add(cmd1)
    i.add(cmd2)
    i.run()

if __name__ == '__main__':
    client_code()
