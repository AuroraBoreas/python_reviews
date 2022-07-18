"#" 

from abc import ABC, abstractmethod


class Template(ABC):
    def operate(self) -> None:
        self.step_01()
        self.step_02()
        self.step_03()
        self.hook_01()
        self.required_step_01()
        self.required_step_02()
        self.required_step_03()
        self.hook_02()
        
    def step_01(self) -> None:
        pass
    def step_02(self) -> None:
        pass
    def step_03(self) -> None:
        pass
    def hook_01(self) -> None:
        pass

    @abstractmethod
    def required_step_01(self) -> None:
        pass
    @abstractmethod
    def required_step_02(self) -> None:
        pass
    @abstractmethod
    def required_step_03(self) -> None:
        pass
    def hook_02(self) -> None:
        pass