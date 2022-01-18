# 

from abc import ABC, abstractmethod


class Template(ABC):
    def operation(self)->None:
        self.do_step_01()
        self.do_step_02()
        self.do_step_03()
        self.hook_01()
        self.required_step_01()
        self.required_step_02()
        self.hook_02()

    def do_step_01(self):
        pass

    def do_step_02(self):
        pass

    def do_step_03(self):
        pass

    def hook_01(self):
        pass

    def hook_02(self):
        pass
    
    @abstractmethod
    def required_step_01(self):
        pass
    
    @abstractmethod
    def required_step_02(self):
        pass