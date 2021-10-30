# chef

from typing import Any

class Receiver:
    def make_food(self, food:str)->None:
        print(f'{food} received, start making...')

class Command:
    def __init__(self, receiver:Receiver, food:str)->None:
        self.receiver = receiver
        self.food = food
    
    def execute(self)->Any:
        self.receiver.make_food(self.food)

class Invoker:
    def __init__(self)->None:
        self.commands = set()

    def add(self, command:Command)->None:
        self.commands.add(command)

    def remove(self, command:Command)->None:
        self.commands.remove(command)

    def run(self)->None:
        for command in self.commands:
            command.execute()

def client_code():
    r = Receiver()
    c1 = Command(r, 'meatball')
    c2 = Command(r, 'coffee')
    c3 = Command(r, 'tea')
    i = Invoker()
    i.add(c1)
    i.add(c2)
    i.add(c3)
    i.run()

if __name__ == '__main__':
    client_code()