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

    def do_step_01(self)->None:
        pass

    def do_step_02(self)->None:
        pass

    def do_step_03(self)->None:
        pass

    def hook_01(self)->None:
        pass
    
    def hook_02(self)->None:
        pass

    @abstractmethod
    def required_step_01(self)->None:
        pass

    @abstractmethod
    def required_step_02(self)->None:
        pass
