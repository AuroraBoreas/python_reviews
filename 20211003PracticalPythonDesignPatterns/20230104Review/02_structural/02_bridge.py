"#" 
from abc import ABC, abstractmethod
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

class IComponent(ABC):
    @abstractmethod
    def do_this(self) -> str:
        raise NotImplementedError()

class Abstract:
    def __init__(self, comp: IComponent) -> None:
        self._comp: IComponent = comp
    
    def operate(self) -> None:
        logging.info(f"{self.__class__} : {self._comp.do_this()} on platformA")

class ExtendedAbstract(Abstract):
    def operate(self) -> None:
        logging.info(f"{self.__class__} : {self._comp.do_this()} on platformB")

class Component(IComponent):
    def do_this(self) -> str:
        return f"{self.__class__} do_this"

def main() -> None:
    c: Component = Component()
    a1: Abstract = Abstract(c)
    e1: ExtendedAbstract = ExtendedAbstract(c)
    a1.operate()
    e1.operate()

if __name__ == '__main__':
    main()
