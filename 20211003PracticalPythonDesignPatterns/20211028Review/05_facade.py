# facade

class Customer:
    def __init__(self, customer_id:int) -> None:
        pass

class Item:
    def __init__(self, barcode:str) -> None:
        pass

class Invoice:
    def __init__(self, customer:Customer) -> None:
        pass

class Facade:
    @staticmethod
    def make_customer(customer_id:int)->Customer:
        return Customer(customer_id)

    @staticmethod
    def make_item(barcode:str)->Item:
        return Item(barcode)

    @staticmethod
    def make_invoice(customer:Customer)->Invoice:
        return Invoice(customer)
