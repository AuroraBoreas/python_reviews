# command
from __future__ import annotations
from typing import List

class Command:
    def __init__(self, receiver:Receiver, request:str)->None:
        self.receiver = receiver
        self.request = request

    def execute(self)->None:
        self.receiver.serve(self.request)

class Receiver:
    def serve(self, request:str)->None:
        print(f'{request} received, started processing..')

class Invoker:
    def __init__(self)->None:
        self.commands:List[Command] = []
    
    def add(self, command:Command)->None:
        self.commands.append(command)
    
    def remove(self, command:Command)->None:
        self.commands.remove(command)
        
    def run(self)->None:
        for command in self.commands:
            command.execute()