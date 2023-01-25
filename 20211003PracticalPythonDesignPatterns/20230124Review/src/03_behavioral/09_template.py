
from abc import ABC, abstractmethod
from typing import Any


class Template(ABC):
    def operate(self) -> Any:
        self.do_step_01()
        self.do_step_02()
        self.do_step_03()
        self.hook_01()
        self.required_step_01()
        self.required_step_02()
        self.hook_02()
    def do_step_01(self) -> Any:
        raise NotImplementedError
    def do_step_02(self) -> Any:
        raise NotImplementedError
    def do_step_03(self) -> Any:
        raise NotImplementedError
    def hook_01(self) -> Any:
        raise NotImplementedError
    def hook_02(self) -> Any:
        raise NotImplementedError
    @abstractmethod
    def required_step_01(self) -> Any:
        raise NotImplementedError
    @abstractmethod
    def required_step_02(self) -> Any:
        raise NotImplementedError
