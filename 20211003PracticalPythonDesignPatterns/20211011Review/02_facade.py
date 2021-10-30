from __future__ import annotations

class Customer:
    def __init__(self, customer_id:int): pass

class Item:
    def __init__(self, item_barcode:str): pass

class Invoice:
    def __init__(self, customer:Customer): pass

...

class Facade:
    @staticmethod
    def make_customer(customer_id:int): return Customer(customer_id)

    @staticmethod
    def make_item(item_barcode:str): return Item(item_barcode)

    @staticmethod
    def make_invoice(customer:Customer): return Invoice(customer)

    ...
