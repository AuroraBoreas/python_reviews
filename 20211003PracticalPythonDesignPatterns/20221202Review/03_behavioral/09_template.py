"#" 

from abc import ABC, abstractmethod
from typing import Any


class Template(ABC):
    def operate(self) -> None:
        self.do_step_01()
        self.do_step_02()
        self.do_step_03()
        self.hook01()
        self.do_required_01()
        self.do_required_02()
        self.hook02()

    def do_step_01(self) -> Any:
        pass

    def do_step_02(self) -> Any:
        pass

    def do_step_03(self) -> Any:
        pass

    def hook01(self) -> Any:
        pass
    
    @abstractmethod
    def do_required_01(self) -> Any:
        pass
    
    @abstractmethod
    def do_required_02(self) -> Any:
        pass

    def hook02(self) -> Any:
        pass