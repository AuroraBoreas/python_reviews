# template method

from abc import abstractmethod


class Template:
    def do_this(self)->None:
        self.step1()
        self.step2()
        self.hook1()
        self.required_step1()
        self.required_step1()
        self.hook2()

    def step1(self)->None:
        pass

    def step2(self)->None:
        pass

    def hook1(self)->None:
        pass

    def hook2(self)->None:
        pass

    @abstractmethod
    def required_step1(self)->None:
        pass

    @abstractmethod
    def required_step2(self)->None:
        pass
