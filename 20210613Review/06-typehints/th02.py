
# user-defined generic types
from typing import TypeVar, Generic
from logging import Logger

T = TypeVar('T')

class LoggedVar(Generic[T]):
    def __init__(self, value: T, name: str, logger: Logger)->None:
        self.name   = name
        self.logger = logger
        self.value  = value
    
    def set(self, new: T)->None:
        self.log('Set ' + repr(self.value))
        self.value = new
    
    def get(self)->T:
        self.log('Get ' + repr(self.value))
        return self.value
    
    def log(self, message: str)->None:
        self.logger.info('{0}:{1}'.format(self.name, message))

# generic type can be passed as type to collections
from typing import TypeVar, Iterator
U = TypeVar('U')
class MyIter(Iterator[U]): ...


from typing import Iterable
class MyIterable(Iterable): # same as Iterable[Any]
    ...


if __name__ == "__main__":
    import logging
    # TODOS: Logger
    logger = Logger(name="ZL", level=logging.INFO)
    log1 = LoggedVar(69, "TS", logger)
    log1.log("is sexy")