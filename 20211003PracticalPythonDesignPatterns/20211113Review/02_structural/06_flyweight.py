# flyweight objects store instrinsic fields only; 

import json
from typing import Dict

class Flyweight:
    def __init__(self, shared_state:str)->None:
        self._shared_state = shared_state

    def do(self, unique_state:str)->None:
        s = json.dumps(self._shared_state)
        u = json.dumps(unique_state)
        print(f'Flyweight: shared ({s}) and unique ({u})', end='')

class FlyweightFactory:
    _flyweights:Dict[str, Flyweight] = {}

    def __init__(self, init_flyweight:Dict) -> None:
        for state in init_flyweight:
            self._flyweights[self.get_key(state)] = Flyweight(state)

    def get_key(self, state:Dict)->str:
        return '_'.join(sorted(state))

    def get_flyweight(self, shared_state:Dict)->Flyweight:
        key = self.get_key(shared_state)
        if not self._flyweights.get(key):
            print(f'FlyweightFactory: {shared_state} not found, creating a new one..')
            self._flyweights[key] = Flyweight(shared_state)
        else:
            print('FlyweightFactory: reusing existing flyweight.')
        return self._flyweights[key]

    def __str__(self)->str:
        print(f'\n\nI have {len(self._flyweights)} flyweights.')
        return '{}'.format('\n'.join(map(str, self._flyweights.keys())), end='')

def client_code()->None:
    f = FlyweightFactory([
        list('abc'),
        list('abd'),
        list('123'),
        list('124'),
    ])
    print(f)
    
    flyweight = f.get_flyweight(list('abe'))
    flyweight.do(list('cy'))

    print(f)

if __name__ == '__main__':
    client_code()