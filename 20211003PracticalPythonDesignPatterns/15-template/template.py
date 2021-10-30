# template method

from abc import ABC, abstractmethod


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
    def base_operation1(self): pass
    def base_operation2(self): pass
    def base_operation3(self): pass

    # operations are uncommon, then request client to implement their own;
    @abstractmethod
    def required_operations1(self): pass

    @abstractmethod
    def required_operations2(self): pass

    # hooks:
    # These are "hooks." Subclasses may override them, but it's not mandatory
    # since the hooks already have default (but empty) implementation. Hooks
    # provide additional extension points in some crucial places of the
    # algorithm.

    def hook1(self): pass
    def hook2(self): pass