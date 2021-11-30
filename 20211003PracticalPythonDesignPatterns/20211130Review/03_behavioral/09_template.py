# 

from abc import ABC, abstractmethod


class Template(ABC):
    def operation(self)->None:
        self.do_step1()
        self.do_step2()
        self.do_step3()
        self.hook1()
        self.required_step1()
        self.required_step2()
        self.hook2()

    def do_step1(self):
        pass
    def do_step2(self):
        pass
    def do_step3(self):
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