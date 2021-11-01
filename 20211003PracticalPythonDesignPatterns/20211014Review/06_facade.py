from __future__ import annotations
from abc import abstractclassmethod

class Customer:
    def __init__(self, customer_id:int)->None:
        pass

class Item:
    def __init__(self, barcode:str)->None:
        pass

class Invoice:
    def __init__(self, customer:Customer)->None:
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

if __name__ == '__main__':
    f = Facade()
    c = f.make_customer(1)
    i = f.make_item('123456789')
    inv = f.make_invoice(c)