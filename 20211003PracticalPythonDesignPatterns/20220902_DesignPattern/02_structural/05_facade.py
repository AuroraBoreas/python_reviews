"#" 

class Customer: pass
class Product: pass
class Invoice: pass

class Facade:
    @staticmethod
    def make_customer() -> Customer: return Customer()

    @staticmethod
    def make_product() -> Product: return Product()

    @staticmethod
    def make_invoice() -> Invoice: return Invoice()

def client_code() -> None:
    f:Facade = Facade()
    f.make_customer()
    f.make_invoice()
    f.make_product()

if __name__ == '__main__':
    client_code()