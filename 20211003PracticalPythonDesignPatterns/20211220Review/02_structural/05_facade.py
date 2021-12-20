# 

class Customer: pass
class Item: pass
class Invoice: pass

class Facade:
    @staticmethod
    def make_customer()->Customer: return Customer()

    @staticmethod
    def make_item()->Item: return Item()

    @staticmethod
    def make_invoice()->Invoice: return Invoice()

    ...