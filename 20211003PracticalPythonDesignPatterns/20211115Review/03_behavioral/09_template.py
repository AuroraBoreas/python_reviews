# template method 

from abc import ABC, abstractmethod


class Template(ABC):
    def do_this(self)->None:
        self.do_step_01()
        self.do_step_02()
        self.do_step_03()
        self.hook1()
        self.required_step_01()
        self.required_step_02()
        self.hook2()
    
    def do_step_01(self):
        pass
    def do_step_02(self):
        pass
    def do_step_03(self):
        pass
    
    def hook1(self):
        pass
    def hook2(self):
        pass

    @abstractmethod
    def required_step_01(self):
        pass
    
    @abstractmethod
    def required_step_02(self):
        pass