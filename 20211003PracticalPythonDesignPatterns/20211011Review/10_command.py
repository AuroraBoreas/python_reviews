from __future__ import annotations


class Command:
    def __init__(self, receiver:Receiver, text:str):
        self.receiver = receiver
        self.text = text

    def execute(self)->None:
        self.receiver.print_message(self.text)

class Receiver:
    def print_message(self, text:str)->None:
        print(f'message received: {text}')

class Invoker:
    def __init__(self):
        self.commands = []

    def add(self, command:Command):
        self.commands.append(command)

    def run(self):
        for command in self.commands:
            command.execute()

if __name__ == '__main__':
    r = Receiver()
    c1 = Command(r, 'command 1')
    c2 = Command(r, 'command 2')
    i = Invoker()
    i.add(c1)
    i.add(c2)
    i.run()
