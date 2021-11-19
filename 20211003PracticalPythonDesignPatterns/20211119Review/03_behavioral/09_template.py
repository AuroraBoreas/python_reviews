# template mathod 

from abc import ABC, abstractmethod


class Template(ABC):
    def operation(self)->None:
        self.step1()
        self.step2()
        self.step3()
        self.hook1()
        self.required_step1()
        self.required_step2()
        self.hook2()
        
    def step1(self):
        pass
    def step2(self):
        pass
    def step3(self):
        pass
    def hook1(self):
        pass
    def hook2(self):
        pass

    @abstractmethod
    def required_step1(self):
        pass
    @abstractmethod
    def required_step2(self):
        pass
