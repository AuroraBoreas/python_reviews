"#" 

class Customer: pass
class Invoice: pass
class Item: pass

class Facade:
    @staticmethod
    def make_customer()->Customer: return Customer()

    @staticmethod
    def make_invoice()->Invoice: return Invoice()

    @staticmethod
    def make_item()->Item: return Item()

    ...