"Python is a protocol orientated language; every top-level function implements its dunder method;" 

from abc import ABC, abstractmethod


class Template(ABC):
    def operate(self) -> None:
        self.do_step_01()
        self.do_step_02()
        self.hook_01()
        self.do_required_01()
        self.do_required_02()
        self.do_required_03()
        self.hook_02()

    def do_step_01(self) -> None:
        pass
    def do_step_02(self) -> None:
        pass
    def hook_01(self) -> None:
        pass
    def hook_02(self) -> None:
        pass
    
    @abstractmethod
    def do_required_01(self) -> None:
        raise NotImplementedError
    
    @abstractmethod
    def do_required_02(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def do_required_03(self) -> None:
        raise NotImplementedError