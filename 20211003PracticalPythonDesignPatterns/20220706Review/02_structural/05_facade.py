# 

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

def client_code() -> None:
    f = Facade()
    cus = f.make_customer()
    inv = f.make_invoice()
    pro = f.make_product()

if __name__ == '__main__':
    client_code()