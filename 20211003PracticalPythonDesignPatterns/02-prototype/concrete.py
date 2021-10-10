from prototype import Prototype
from copy import deepcopy

class Concrete(Prototype):
    def clone(self):
        return deepcopy(self)
