
class Customer:
    def __init__(self, customer_id:int)->None: pass

class Item:
    def __init__(self, item_barcode:str)->None: pass

class Invoice:
    def __init__(self, customer:Customer)->None: pass

...

class Facade:
    @staticmethod
    def make_customer(customer_id:int)->object:
        return Customer(customer_id)

    @staticmethod
    def make_item(item_barcode:str)->object:
        return Item(item_barcode)

    @staticmethod
    def make_invoice(customer:Customer)->object:
        return Invoice(customer)

    ...