# facade pattern is used specifically to create a complexity-limiting interface to a sub-system or collection of sub-system;

class Invoice:
    def __init__(self, customer): pass

class Customer:
    def __init__(self, customer_id): pass

class Item:
    def __init__(self, item_barcode): pass

class Facade:
    @staticmethod
    def make_invoice(customer): return Invoice(customer)

    @staticmethod
    def make_customer(customer_id): return Customer(customer_id)

    @staticmethod
    def make_item(item_barcode): return Item(item_barcode)

    ...
