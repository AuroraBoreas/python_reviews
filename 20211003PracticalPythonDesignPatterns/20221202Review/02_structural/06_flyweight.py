"#" 

import json
from typing import Dict, List


class Flyweight:
    def __init__(self, shared:str) -> None:
        self._shared = shared

    def operate(self, unique:str) -> str:
        u = json.dumps(unique)
        s = json.dumps(self._shared)
        return f'{self.__class__} : shared -> {s}; unique -> {u}'

class FlyweightFactory:
    flyweights:Dict[str, Flyweight] = dict()

    def __init__(self, init_flyweights:List) -> None:
        for state in init_flyweights:
            self.flyweights[self.get_key(state)] = Flyweight(state)
    
    def get_key(self, shared:List) -> str:
        return '_'.join(sorted(shared))

    def get_flyweight(self, shared:List) -> Flyweight:
        key = self.get_key(shared)
        if not key in self.flyweights:
            print(f'{self.__class__} : {shared} not found, create a new one..')
            self.flyweights[key] = Flyweight(shared)
        else:
            print(f'{self.__class__} : userping the existing one')
        return self.flyweights[key]

    def list_flyweights(self) -> str:
        return 'flyweights:\n{}'.format("\n".join(self.flyweights.keys()))

def add_car_to_police_database(
    factory:FlyweightFactory,
    plate:str,
    owner:str,
    brand:str,
    model:str,
    color:str) -> None:
    flyweight = factory.get_flyweight([brand, model, color])
    print(flyweight.operate([plate, owner]))

def client_code() -> None:
    factory = FlyweightFactory([
        ["Chevrolet", "Camaro2018", "pink"],
        ["Mercedes Benz", "C300", "black"],
        ["Mercedes Benz", "C500", "red"],
        ["BMW", "M5", "red"],
        ["BMW", "X6", "white"],
    ])
    print(factory.list_flyweights())

if __name__ == '__main__':
    client_code()