# facade

class Customer:
    def __init__(self): pass

class Item:
    def __init__(self): pass

class Invoice:
    def __init__(self): pass

class Facade:
    @staticmethod
    def make_customer()->None:
        return Customer()

    @staticmethod
    def make_item()->None:
        return Item()

    @staticmethod
    def make_invoice()->None:
        return Invoice()
