"Python is a protocoal orientated lang; every top-level function has a corresponding dunder method implemented;" 

class Customer: pass
class Invoice: pass
class Product: pass

class Facade:
    @staticmethod
    def make_customer() -> Customer: return Customer()
    
    @staticmethod
    def make_invoice() -> Invoice: return Invoice()

    @staticmethod
    def make_product() -> Product: return Product()