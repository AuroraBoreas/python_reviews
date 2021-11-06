# facade

class Customer:
    def __init__(self) -> None:
        pass

class Item:
    def __init__(self) -> None:
        pass

class Invoice:
    def __init__(self) -> None:
        pass

class Facade:
    @staticmethod
    def make_customer() -> Customer: pass

    @staticmethod
    def make_item()->Item: pass

    @staticmethod
    def make_invoice()->Invoice: pass
