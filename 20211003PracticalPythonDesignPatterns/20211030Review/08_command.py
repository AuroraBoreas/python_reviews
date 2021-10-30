# chef
from __future__ import annotations

class Command:
    def __init__(self, rec:Receiver, food:str)->None:
        self.receiver = rec
        self.food = food
    
    def execute(self)->None:
        self.receiver.cook(self.food)

class Receiver:
    def cook(self, food:str)->None:
        print(f'received, start {food}')

class Invoker:
    def __init__(self)->None:
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
    c3 = Command(r, 'command 3')
    invoker = Invoker()
    invoker.add(c1)
    invoker.add(c2)
    invoker.add(c3)
    invoker.run()

if __name__ == '__main__':
    client_code()