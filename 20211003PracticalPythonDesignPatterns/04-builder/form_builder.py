
import abc

class Director(metaclass=abc.ABCMeta):
    def __init__(self):
        self._builder = None
    
    def set_builder(self, builder):
        self.set_builder = builder

    @abc.abstractmethod
    def construct(self):
        raise NotImplementedError()

    def get_constructed_object(self):
        return self._builder.constructed_object

class Builder(metaclass=abc.ABCMeta):
    def __init__(self, constructed_object):
        self.constructed_object = constructed_object
    
class Product:
    def __init__(self):
        pass
    def __repr__(self):
        pass
    
class ConcreteBuilder(Builder):
    pass

class ConcreteDirector(Director):
    pass
