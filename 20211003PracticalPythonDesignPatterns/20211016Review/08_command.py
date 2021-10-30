from __future__ import annotations
from logging import NOTSET


class Command:
    def __init__(self, receiver:Receiver, text:str)->None:
        self.receiver = receiver
        self.text = text

    def execute(self):
        self.receiver.print_msg(self.text)

class Receiver:
    def print_msg(self, text:str):
        print(f'message received: {text}')

class Invoker:
    def __init__(self):
        self.commands = []

    def add(self, command:Command):
        self.commands.append(command)

    def run(self, text:str):
        for command in self.commands:
            command.execute(text)