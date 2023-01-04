"#" 

class Customer: ...
class Invoice: ...
class Product: ...

class Facade:
    @staticmethod
    def make_customer() -> Customer:
        return Customer()

    @staticmethod
    def make_invoice() -> Invoice:
        return Invoice()

    @staticmethod
    def make_product() -> Product:
        return Product()

def client_code(f: Facade) -> None:
    f.make_customer()
    f.make_invoice()
    f.make_product()

def main() -> None:
    f: Facade = Facade()
    client_code(f)

if __name__ == '__main__':
    main()
