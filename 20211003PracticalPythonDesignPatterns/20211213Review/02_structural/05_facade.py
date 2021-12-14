# 

from abc import abstractmethod


class Customer: pass
class Item: pass
class Invoice: pass

class Facade:
    @abstractmethod
    def make_customer()->Customer: return Customer()

    @abstractmethod
    def make_item()->Item: return Item()

    @abstractmethod
    def make_invoice()->Invoice: return Invoice()

    ...