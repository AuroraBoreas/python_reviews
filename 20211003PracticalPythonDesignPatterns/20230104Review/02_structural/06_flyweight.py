"#" 
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
import json

class Flyweight:
    def __init__(self, shared: str) -> None:
        self._shared: str = shared

    def operate(self, unique: str) -> str:
        s: str = json.dumps(self._shared)
        u: str = json.dumps(unique)
        return f"{self.__class__} : shared -> ({s}), unique -> ({u})"

class FlyweightFactory:
    __flyweights: dict[str, Flyweight] = dict()

    def __init__(self, init_flyweights: list[str]) -> None:
        for init_flyweight in init_flyweights:
            self.__flyweights[self.get_status(init_flyweight)] = Flyweight(init_flyweight)

    def get_status(self, shared: list[str]) -> str:
        return '_'.join(sorted(shared))

    def get_flyweight(self, shared: list[str]) -> str:
        key: str = self.get_status(shared)
        if key not in self.__flyweights:
            logging.info(f'{shared} is not found, creating a new one')
            self.__flyweights[key] = Flyweight(shared)
        else:
            logging.info(f'{shared} existed, reusing the existed one')
        return self.__flyweights[key]

    def show_flyweights(self) -> str:
        return "flyweights:{}".format("\n".join(map(str, self.__flyweights.keys())))