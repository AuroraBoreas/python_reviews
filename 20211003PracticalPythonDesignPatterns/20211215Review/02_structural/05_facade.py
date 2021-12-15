# 

class Customer: pass

class Item: pass

class Invoice: pass

class Facade:
    @staticmethod
    def make_customer()->Customer: pass

    @staticmethod
    def make_item()->Item: pass

    @staticmethod
    def make_invoice()->Invoice: pass

    ...