# template method

from abc import ABCMeta, abstractmethod


class Template:
    __metaclass__ = ABCMeta

    def do_work(self):
        self.step1()
        self.step2()
        self.required_step1()
        self.hook1()
        self.required_step2()
        self.hook2()

    def step1(self)->None:
        pass
    
    def step2(self)->None:
        pass

    def hook1(self)->None:
        pass

    def hook2(self)->None:
        pass

    @abstractmethod
    def required_step1(self):
        raise NotImplementedError()

    @abstractmethod
    def required_step2(self):
        raise NotImplementedError()