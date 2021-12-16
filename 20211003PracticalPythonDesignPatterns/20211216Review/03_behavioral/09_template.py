# 

from abc import ABC, abstractmethod


class Template(ABC):
    def operation(self)->None:
        self.do_step_01()
        self.do_step_02()
        self.do_step_03()
        self.hook01()
        self.required_step_01()
        self.required_step_02()
        self.hook02()

    def do_step_01(self):
        pass

    def do_step_02(self):
        pass

    def do_step_03(self):
        pass

    def hook01(self):
        pass
    
    def hook02(self):
        pass
    
    @abstractmethod
    def required_step_01(self):
        pass
    
    @abstractmethod
    def required_step_02(self):
        pass