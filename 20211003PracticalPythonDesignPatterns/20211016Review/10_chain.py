
from __future__ import annotations
from abc import ABCMeta, abstractmethod
from typing import Union

class IHanlder(metaclass=ABCMeta):
    @abstractmethod
    def set_next(self, handler:IHanlder)->IHanlder: pass

    @abstractmethod
    def handle(self, request)->Union[None, str]: pass

class ConcreteHanlder(IHanlder):
    _next_handler:IHanlder = None

    def set_next(self, handler: IHanlder) -> IHanlder:
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request)->Union[None, str]:
        if self._next_handler:
            return self._next_handler.handle(request)
        return None

class MonkeyHandler(ConcreteHanlder):
    def handle(self, request) -> Union[None, str]:
        if request == 'banana':
            return f'Monkey, i will eat the {request}'
        return super().handle(request)

class SquirrelHandler(ConcreteHanlder):
    def handle(self, request) -> Union[None, str]:
        if request == 'nut':
            return f'Squirrel, i will eat the {request}'
        return super().handle(request)

class DogHandler(ConcreteHanlder):
    def handle(self, request) -> Union[None, str]:
        if request == 'meatball':
            return f'Dog, i will eat the {request}'
        return super().handle(request)

def client_code(handler:IHanlder):
    for food in ['nut', 'meatball', 'coffee']:
        print(f'\nwho wants {food}')
        rv = handler.handle(food)
        if rv:
            print(f'   {rv}', end='')
        else:
            print(f'   {food} was left untouched', end='')

if __name__ == '__main__':
    m = MonkeyHandler()
    d = DogHandler()
    s = SquirrelHandler()

    print('m > d > s')
    m.set_next(d).set_next(s)

    # client_code(m)
    rv = m.handle('meatball')
    print('result : {}'.format(rv))