from typing import Dict, Union, Optional

from computer import Computer

class ResaleShop:
    itemID: int = 0
    inventory : Dict[int, Computer] = {}

    def __init__(self, item_id: int, inventory: Dict):
        self.itemID = item_id
        self.inventory = inventory

    def buy(self, computer: object):
        self.itemID += 1
        self.inventory[self.itemID] = computer
        return self.itemID

    def sell(self, item_id: int):
        if item_id in self.inventory:
            del self.inventory[item_id]
            print(f"Item {item_id} sold.")
        else:
            print(f"Item {item_id} not found. Please select another item to sell.")

    def refurbish(self, item_id: int, new_os: Optional[str] = None):
        if item_id in self.inventory:
            self.inventory[item_id].updatePrice()
            if new_os is not None:
                self.inventory[item_id].updateOS(new_os)
        else:
            print("Item", item_id, "not found. Please select another item to refurbish.")

def main():
    pass

if __name__ == "__main__": main()