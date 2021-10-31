# template method

from abc import ABC, abstractmethod

a = int(1)

print(f'{a:.2f}')

class AbstractClass(ABC):
    def template_method(self)->None:
        self.base_operation1()
        self.required_operations1()
        self.base_operation2()
        self.hook1()
        self.required_operations2()
        self.base_operation3()
        self.hook2()

    # operations are common, then have default implementation;
    def base_operation1(self): print(f'{self.__class__} says: I am doing the bulk of the work')
    def base_operation2(self): print(f'{self.__class__} says: but let subclass override some operations')
    def base_operation3(self): print(f'{self.__class__} says: I am doing the bulk of the work anyway')

    # operations are uncommon, then request client to implement their own;
    @abstractmethod
    def required_operations1(self): pass

    @abstractmethod
    def required_operations2(self): pass

    # hooks:
    # These are "hooks." Subclasses may override them, but it's not manda tory
    # since the hooks already have default (but empty) implementat00ion. Hooks
    # provide additional extension points in some crucial places of the
    # algorithm.

    def hook1(self): pass
    def hook2(self): pass

class ConcreteClass1(AbstractClass):
    def required_operations1(self):
        print(f'{self.__class__} says: implemented operation1')

    def required_operations2(self):
        print(f'{self.__class__} says: implemented operation2')

class ConcreteClass2(AbstractClass):
    def required_operations1(self):
        print(f'{self.__class__} says: implemented operation1')

    def required_operations2(self):
        print(f'{self.__class__} says: implemented operation2')
    
    def hook1(self):
        print(f'{self.__class__} says: overridden operation2')

def client_code(ab:AbstractClass)->None:
    ab.template_method()


if __name__ == '__main__':
    client_code(ConcreteClass1())
    client_code(ConcreteClass2())