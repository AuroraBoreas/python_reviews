# chef

from typing import Any, ContextManager


class Receiver:
    def make_food(self, request:str)->None:
        print(f'{self.__class__} start making {request}')

class Command:
    def __init__(self, rec:Receiver, request:str)->None:
        self.rec = rec
        self.request = request

    def execute(self)->Any:
        self.rec.make_food(self.request)

class Invoker:
    def __init__(self)->None:
        self.commands = []

    def add(self,command:Command)->None:
        self.commands.append(command)

    def run(self)->Any:
        for command in self.commands:
            command.execute()

def client_code()->None:
    r = Receiver()
    c1 = Command(r, 'coffee')
    c2 = Command(r, 'creame pie')
    i = Invoker()
    i.add(c1)
    i.add(c2)
    i.run()

if __name__ == '__main__':
    client_code()