from typing import Dict, Union, Optional

class ResaleShop:
    itemID: int = 0
    inventory : Dict[int, Dict[str, Union[str, int, bool]]] = {}

    def __init__(self, item, inventory):
        self.itemID = item
        self.inventory = inventory

    def buy(self, computer):
        self.itemID += 1
        self.inventory[self.itemID] = computer
        return self.itemID

    def sell():
        pass

    def refurbish():
        pass
    # What methods will you need?