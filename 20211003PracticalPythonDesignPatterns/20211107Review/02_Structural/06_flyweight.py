# flyweight: stores instrinsic fields only; accept extrinsic fields as parameters
import json
from typing import Dict

class Flyweight:
    def __init__(self, shared_state:str)->None:
        self.shared_state = shared_state

    def operation(self, unique_state:str)->None:
        s = json.dumps(self.shared_state)
        u = json.dumps(unique_state)
        print(f'Flyweight: shared_state->{s}, unique_state->{u}')

class FlyweightFactory:
    _flyweights: Dict[str, Flyweight] = {}
    
    def __init__(self, initial_flyweights:Dict) -> None:
        for state in initial_flyweights:
            self._flyweights[self.get_key(state)] = Flyweight(state)
    
    def get_key(self, state:Dict)->str:
        return '_'.join(sorted(state))

    def get_flyweight(self, shared_state:Dict)->Flyweight:
        key = self.get_key(shared_state)
        if self._flyweights.get(key):
            print(f'FlyweightFactory: cannot found the flyweight, creating a new one..')
            self._flyweights[key] = Flyweight(shared_state)
        else:
            print('FlyweightFactory: reusing existing flyweight..')
        return self._flyweights[key]

    def list_flyweight(self)->None:
        count = len(self._flyweights)
        print(f'FlyweightFactory: I have{count} flyweights:')
        print('\n'.join(map(str, self._flyweights.keys())), end='')

def client_code(f:FlyweightFactory, plates:str, owner:str, brand:str, model:str, color:str)->None:
    print('\n\nClient: adding a car to database')
    flyweight = f.get_flyweight([brand, model, color])
    flyweight.operation([plates, owner])
