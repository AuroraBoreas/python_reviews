# facade

class Customer:
    def __init__(self, cid:int)->None:
        pass

class Item:
    def __init__(self, barcode:str) -> None:
        pass

class Invoice:
    def __init__(self, customer:Customer)->None:
        pass

class Facade:
    @staticmethod
    def make_customer(cid:int)->Customer:
        return Customer(cid)

    @staticmethod
    def make_item(barcode:str)->Item:
        return Item(barcode)

    @staticmethod
    def make_invoice(customer:Customer)->Invoice:
        return Invoice(customer)