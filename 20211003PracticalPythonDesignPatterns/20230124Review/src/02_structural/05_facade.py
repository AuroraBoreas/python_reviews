class Customer: pass
class Invoice: pass
class Product: pass

class Facade:
    @staticmethod
    def make_customer() -> Customer: pass
    @staticmethod
    def make_invoice() -> Invoice: pass
    @staticmethod
    def make_product() -> Product: pass

